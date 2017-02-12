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


def object_factory(kind):
    """Generator of submissions from the database that have not yet been posted"""
    if kind == 'submission':
        c.execute('''SELECT * FROM submissions WHERE posted=0''')
    elif kind == 'root':
        c.execute('''SELECT * FROM comments WHERE is_root=1 AND posted=0''')
    elif kind == 'child':
        c.execute('''SELECT * FROM comments WHERE is_root=0 AND posted=0''')
    for item in c.fetchall():
        yield item


def handle(item, kind):
    if kind == 'submission':
        repost_id = post_sub(item)
        mark_posted(item, repost_id, kind)
    else:
        parent = parent_exists(item, kind)
        if not parent:
            return
        repost_id = post_comment(item, parent, kind)
        mark_posted(item, repost_id, kind)


def post_sub(submission):
    """Cross post the submission as a selftext or link and return the repost_id.
    Create a sticky comment with the author if the submission is a link."""
    title = submission[5]
    text = submission[6] if submission[6] else '(No text)'
    comment_body = text + author_signature(submission[4])
    link = submission[7]
    try:
        destination = reddit.subreddit(config.dest)
        if link:
            post = destination.submit(title=title, url=link, send_replies=False)
            create_sticky(submission[4], post)
        else:
            post = destination.submit(title=title, selftext=comment_body, send_replies=False)
    except Exception as error:
        logger.exception(error)
        sys.exit()
    else:
        return post.id


def create_sticky(author, repost):
    """Make a sticky comment with the authors name. Used for link submissions only"""
    try:
        comment = repost.reply(author_signature(author))
    except Exception as error:
        logger.exception(error)
        sys.exit()
    else:
        comment.mod.distinguish(sticky=True)
        return


def post_comment(comment, parent, kind):
    comment_body = comment[5] + author_signature(comment[4])
    try:
        if kind == 'root':
            repost = reddit.submission(parent).reply(comment_body)
        else:
            repost = reddit.comment(parent).reply(comment_body)
    except Exception as error:
        logger.exception(error)
        sys.exit()
    else:
        return repost.id


def parent_exists(comment, kind):
    parent_id = comment[6]
    if kind == 'root':
        sql = '''SELECT repost_id FROM submissions WHERE id=(?)'''
    else:
        sql = '''SELECT repost_id FROM comments WHERE id=(?)'''
    c.execute(sql, (parent_id,))
    result = c.fetchone()
    if result:
        repost_id = result[0]
        if repost_id:
            return repost_id
    return None


def mark_posted(item, repost_id, kind):
    if kind == 'submission':
        sql = '''UPDATE submissions SET posted=(?), repost_id=(?) WHERE id=(?)'''
    else:
        sql = '''UPDATE comments SET posted=(?), repost_id=(?) WHERE id=(?)'''
    c.execute(sql, (True, repost_id, item[1]))
    conn.commit()


def author_signature(author):
    """Anonymize the the author's name"""
    anon = author[:2] + ('*' * (len(author) - 4)) + author[-2:]
    return '\n\nWritten by: {}'.format(anon)


def run():
    """Cross post all new submissions, then root comments, then child comments"""
    while True:
        kinds = ['submission', 'root', 'child']
        for kind in kinds:
            stream = object_factory(kind)
            for item in stream:
                handle(item, kind)
        sleep(loiter)

if __name__ == '__main__':
    logger.info('Start')
    run()
