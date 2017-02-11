from time import sleep
import prawcore
import logging
import sqlite3
import config
import praw
import sys

logger = logging.getLogger('Poster')
logging.basicConfig(filename=config.log_file,
                    filemode=config.mode,
                    level=config.level,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger.disabled = config.disabled
try:
    reddit = praw.Reddit(**config.poster)
except prawcore.exceptions.OAuthException as e:
    logger.exception(e)
    logger.critical('Authentication failed.')
    sys.exit()
conn = sqlite3.connect(config.db_file)
c = conn.cursor()
loiter = config.loiter
max_restarts = config.max_restarts


# --- Post submissions
def new_subs():
    """Generator of submissions from the database that have not yet been posted"""
    c.execute('''SELECT * FROM submissions WHERE posted=0''')
    for submission in c.fetchall():
        yield submission


def post_sub(submission):
    """Cross post the submission as a selftext or link and return the repost_id.
    Create a sticky comment with the author if the submission is a link."""
    title = submission[5]
    text = submission[6] if submission[6] else '(No text)'
    comment_body = text + author_signature(submission[4])
    link = submission[7]
    destination = reddit.subreddit(config.dest)
    if link:
        post = destination.submit(title=title, url=link, send_replies=False)
        create_sticky(submission[4], post)
    else:
        post = destination.submit(title=title, selftext=comment_body, send_replies=False)
    return post.id


def mark_sub_posted(sub, repost_id):
    """Mark the submission as posted in the database and update the row with the repost_id"""
    c.execute('''UPDATE submissions SET posted=(?), repost_id=(?) WHERE id=(?)''',
              (True, repost_id, sub[1]))
    conn.commit()


def create_sticky(author, repost):
    """Make a sticky comment with the authors name. Used for link submissions only"""
    comment = repost.reply(author_signature(author))
    comment.mod.distinguish(sticky=True)


# --- Handle root comments
def new_root_comments():
    """Generator of root level comments from the database that have not yet been posted"""
    c.execute('''SELECT * FROM comments WHERE is_root=1 AND posted=0''')
    for comment in c.fetchall():
        yield comment


def parent_submission(comment):
    """Verify that the parent submission has been posted already and return the repost_id if so"""
    sub_id = comment[7]
    c.execute('''SELECT repost_id FROM submissions WHERE id=(?)''', (sub_id,))
    entry = c.fetchone()
    if entry and entry[0]:
        return entry[0]
    return False


def post_root_comment(parent, root_comment):
    """Build the comment body from the original text and the authors name and post the comment
    Return the post_id to be used to update the database"""
    comment_body = root_comment[5] + author_signature(root_comment[4])
    repost = reddit.submission(parent).reply(comment_body)
    return repost.id


def mark_root_posted(root_comment, repost_id):
    """Mark the comment as posted in the database and update the row with the repost_id"""
    c.execute('''UPDATE comments SET posted=(?), repost_id=(?) WHERE id=(?)''',
              (True, repost_id, root_comment[1]))
    conn.commit()


# --- Handle child comments
def new_child_comments():
    """Generator of child level comments from the database that have not yet been posted"""
    c.execute('''SELECT * FROM comments WHERE is_root=0 AND posted=0''')
    for comment in c.fetchall():
        yield comment


def parent_comment(child_comment):
    """Verify that the parent comment has been posted already and return the repost_id if so"""
    parent_comm = child_comment[6]
    c.execute('''SELECT repost_id FROM comments WHERE id=(?)''', (parent_comm,))
    entry = c.fetchone()
    if entry and entry[0]:
        return entry[0]
    return False


def post_child_comment(parent, child_comment):
    """Build the comment body from the original text and the authors name and post the comment
    Return the post_id to be used to update the database"""
    comment_body = child_comment[5] + author_signature(child_comment[4])
    repost = reddit.submission(parent).reply(comment_body)
    return repost.id


def mark_child_posted(child_comment, repost_id):
    """Mark the comment as posted in the database and update the row with the repost_id"""
    c.execute('''UPDATE comments SET posted=(?), repost_id=(?) WHERE id=(?)''',
              (True, repost_id, child_comment[1]))
    conn.commit()


# --- Main
def author_signature(author):
    """Anonymize the the author's name"""
    anon = author[:2] + ('*' * (len(author) - 4)) + author[-2:]
    return '\n\nWritten by: {}'.format(anon)


def run():
    """Cross post all new submissions, then root comments, then child comments"""
    for sub in new_subs():
        repost_id = post_sub(sub)
        mark_sub_posted(sub, repost_id)

    for root_comment in new_root_comments():
        parent = parent_submission(root_comment)
        if parent:
            repost_id = post_root_comment(parent, root_comment)
            mark_root_posted(root_comment, repost_id)

    for child_comment in new_child_comments():
        parent = parent_comment(child_comment)
        if parent:
            repost_id = post_child_comment(parent, child_comment)
            mark_child_posted(child_comment, repost_id)


def main():
    """Create a log entry that the bot has started, then execute the script once per the loiter time"""
    logger.info('Start')
    restarts = 0
    while restarts < max_restarts:
        try:
            run()
            sleep(loiter)
        except prawcore.exceptions.OAuthException as e:
            logger.exception(e)
            logger.critical('Authentication failed. Shutting down.')
            break
        except prawcore.exceptions.RequestException as e:
            logger.exception(e)
            restarts += 1
            sleep(loiter)
            continue
        except prawcore.exceptions.ResponseException as e:
            logger.exception(e)
            restarts += 1
            sleep(loiter)
            continue
        except Exception as e:
            logger.exception(e)
            restarts += 1
            sleep(loiter)
            continue
        else:
            continue
    else:  # Only entered if the while condition becomes False
        logger.error('Max restarts exceeded')
    logger.info('Stop')


if __name__ == '__main__':
    main()
