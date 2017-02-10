#! /usr/bin/python3.5

from time import sleep
import prawcore
import logging
import sqlite3
import config
import praw

logger = logging.getLogger('Poster')
reddit = praw.Reddit(**config.poster)

restarts = 0
loiter = config.loiter
max_restarts = config.max_restarts

logging.basicConfig(filename=config.log_file,
                    filemode=config.mode,
                    level=config.level,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger.disabled = config.disabled
conn = sqlite3.connect(config.db_file)
c = conn.cursor()


# --- Post submissions
def new_subs():
    """Get all new submissions and post them"""
    c.execute('''SELECT * FROM submissions WHERE posted=0''')
    for submission in c.fetchall():
        yield submission


def post_sub(submission):
    """Cross post the submission as a selftext or link and return the repost_id"""
    title = submission[5]
    text = submission[6]
    link = submission[7]
    destination = reddit.subreddit(config.dest)
    if text:
        post = destination.submit(title=title, selftext=text, send_replies=False)
    else:
        post = destination.submit(title=title, url=link, send_replies=False)
        create_sticky(submission[4], post)
    return post.id


def mark_sub_posted(sub, repost_id):
    """Update posted and repost_id"""
    c.execute('''UPDATE submissions SET posted=(?), repost_id=(?) WHERE id=(?)''',
              (True, repost_id, sub[1]))
    conn.commit()


def create_sticky(author, repost):
    comment = repost.reply(author_signature(author))
    comment.mod.distinguish(sticky=True)
    pass


# --- Handle root comments
def new_root_comments():
    """Get all new root comments and yield them"""
    c.execute('''SELECT * FROM comments WHERE is_root=1 AND posted=0''')
    for comment in c.fetchall():
        yield comment


def parent_submission(comment):
    sub_id = comment[7]
    c.execute('''SELECT repost_id FROM submissions WHERE id=(?)''', (sub_id,))
    entry = c.fetchone()
    if entry and entry[0]:
        return entry[0]
    return False


def post_root_comment(parent, root_comment):
    comment_body = root_comment[5] + author_signature(root_comment[4])
    repost = reddit.submission(parent).reply(comment_body)
    return repost.id


def mark_root_posted(root_comment, repost_id):
    """Update as posted and insert repost_id"""
    c.execute('''UPDATE comments SET posted=(?), repost_id=(?) WHERE id=(?)''',
              (True, repost_id, root_comment[1]))
    conn.commit()


# --- Handle child comments
def new_child_comments():
    """Get all new child comments and yield them"""
    c.execute('''SELECT * FROM comments WHERE is_root=0 AND posted=0''')
    for comment in c.fetchall():
        yield comment


def parent_comment(child_comment):
    """Return the parent comment origi"""
    parent_comm = child_comment[6]
    c.execute('''SELECT repost_id FROM comments WHERE id=(?)''', (parent_comm,))
    entry = c.fetchone()
    if entry and entry[0]:
        return entry[0]
    return False


def post_child_comment(parent, child_comment):
    comment_body = child_comment[5] + author_signature(child_comment[4])
    repost = reddit.submission(parent).reply(comment_body)
    return repost.id


def mark_child_posted(child_comment, repost_id):
    """Update as posted and insert repost_id"""
    c.execute('''UPDATE comments SET posted=(?), repost_id=(?) WHERE id=(?)''',
              (True, repost_id, child_comment[1]))
    conn.commit()


# --- Main
def author_signature(author):
    """Anonymize the the author's name"""
    anon = author[:2] + ('*' * (len(author) - 4)) + author[-2:]
    return '\n\nWritten by: {}'.format(anon)


def main():
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


if __name__ == '__main__':
    logger.info('Start')
    while restarts < max_restarts:
        try:
            main()
            sleep(loiter)
        except prawcore.exceptions.OAuthException as e:
            logger.exception(e)
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
        logger.info('Max restarts exceeded')
    logger.info('Stop')
    if config.admin_user:
        reddit.redditor(config.admin_user).message('YOUR BOT HAS STOPPED',
                                                   'Your Poster bot has malfunctioned.\n'
                                                   'Please review the activity log for errors.')
