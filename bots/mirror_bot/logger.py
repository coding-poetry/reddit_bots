#! /usr/bin/python3.5

from collections import deque
from time import sleep
import threading
import prawcore
import logging
import sqlite3
import config
import praw

logger = logging.getLogger('Logger')
reddit = praw.Reddit(**config.logger)
restarts = 0
loiter = config.loiter
max_restarts = config.max_restarts
source = config.src
logging.basicConfig(filename=config.log_file,
                    filemode=config.mode,
                    level=config.level,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger.disabled = config.disabled
conn = sqlite3.connect(config.db_file)
c = conn.cursor()


def build_db():
    """Create the tables"""
    c.execute('''CREATE TABLE IF NOT EXISTS submissions(
    posted, id, repost_id, self, auth, title, text, link)''')
    c.execute('''CREATE TABLE IF NOT EXISTS comments(
    posted, id, repost_id, is_root, auth, text, parent_id, sub_id)''')
    conn.commit()


def submission_exists(submission):
    """Query the existence of a submission"""
    c.execute('''SELECT id FROM submissions WHERE id=(?) LIMIT 1''', (submission.id,))
    if c.fetchone():
        return True
    return False


def comment_exists(comment):
    """Query the existence of a comment"""
    c.execute('''SELECT id FROM comments WHERE id=(?) LIMIT 1''', (comment.id,))
    if c.fetchone():
        return True
    return False


def store_submission(submission):
    """Insert submission info into the database"""
    _id = submission.id
    _self = True if submission.is_self == 1 else False
    _auth = submission.author.name
    _title = submission.title
    _link = submission.url if not _self else None
    _text = submission.selftext if submission.selftext else None
    tries = 0
    while tries < 5:
        try:
            c.execute('''INSERT INTO submissions
                (posted, id, repost_id, self, auth, title, text, link) VALUES (?,?,?,?,?,?,?,?)''',
                (False, _id, None, _self, _auth, _title, _text, _link))
            conn.commit()
        except sqlite3.OperationalError as error:
            logger.exception(error)
            sleep(2)
            continue
        else:
            break
    else:
        logger.log(50, 'DATABASE ERROR. UPDATE FAILED')


def store_comment(comment):
    """Insert comment data into the database"""
    if comment.edited:
        return
    _id = comment.id
    _is_root = comment.is_root
    _auth = comment.author.name
    _text = comment.body
    _parent_id = comment.parent().id
    _sub_id = comment.submission.id
    tries = 0
    while tries < 5:
        try:
            c.execute('''INSERT INTO comments
                (posted, id, repost_id, is_root, auth, text, parent_id, sub_id)
                VALUES (?,?,?,?,?,?,?,?)''',
                (False, _id, None, _is_root, _auth, _text, _parent_id, _sub_id))
            conn.commit()
        except sqlite3.OperationalError as error:
            logger.exception(error)
            sleep(2)
            continue
        else:
            break
    else:
        logger.log(50, 'DATABASE ERROR. UPDATE FAILED')


def _feed_subs_to_queue(monitored_sub, queue):
    """Stream all submissions and put them into the queue.
    Submissions are stored in a tuple with a 0."""

    subreddit = reddit.subreddit(monitored_sub)
    while True:
        try:
            for sub in subreddit.stream.submissions():
                queue.append((sub, 0))
        except Exception as error:
            logger.exception(error)
            continue


def _feed_comms_to_queue(monitored_sub, queue):
    """Stream all comments and put them into the queue.
    Comments are stored in a tuple with a 1."""

    subreddit = reddit.subreddit(monitored_sub)
    while True:
        try:
            for com in subreddit.stream.comments():
                queue.append((com, 1))
        except Exception as error:
            logger.exception(error)
            continue


def sub_com_stream(queue):
    """Stream the comments and submissions from the queue"""
    while True:
        try:
            entry = queue.pop()
        except IndexError:
            continue
        else:
            yield entry


def main():
    """Create a queue to use as a funnel, start the threads and dispatch as needed"""
    q = deque()
    s_thread = threading.Thread(target=_feed_subs_to_queue, args=(source, q), daemon=True)
    c_thread = threading.Thread(target=_feed_comms_to_queue, args=(source, q), daemon=True)
    s_thread.start()
    c_thread.start()
    for entry in sub_com_stream(q):
        if entry[1] == 0 and not submission_exists(entry[0]):
            store_submission(entry[0])
        elif entry[1] == 1 and not comment_exists(entry[0]):
            store_comment(entry[0])
        else:
            continue


if __name__ == '__main__':
    logger.info('Start')
    build_db()
    while restarts < max_restarts:
        try:
            main()
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
