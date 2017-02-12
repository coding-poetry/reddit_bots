from collections import deque
from time import sleep
import threading
import prawcore
import logging
import sqlite3
import config
import praw
import sys

logger = logging.getLogger('Logger')
loiter = config.loiter
logging.basicConfig(filename=config.log_file,
                    filemode=config.mode,
                    level=config.level,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger.disabled = config.disabled
try:
    reddit = praw.Reddit(**config.logger)
except prawcore.exceptions.OAuthException as e:
    logger.exception(e)
    logger.critical('Authentication failed.')
    sys.exit()
conn = sqlite3.connect(config.db_file)
c = conn.cursor()
max_restarts = config.max_restarts
source = config.src


def build_db():
    """Create the tables for submissions and comments"""
    c.execute('''CREATE TABLE IF NOT EXISTS submissions(
    posted, id, repost_id, self, auth, title, text, link)''')
    c.execute('''CREATE TABLE IF NOT EXISTS comments(
    posted, id, repost_id, is_root, auth, text, parent_id, sub_id)''')
    conn.commit()


def object_exists(_object, submission=True):
    """Query the existence of a submission or comment. Default to look for a submission."""
    if submission:
        c.execute('''SELECT id FROM submissions WHERE id=(?) LIMIT 1''', (_object.id,))
    else:
        c.execute('''SELECT id FROM comments WHERE id=(?) LIMIT 1''', (_object.id,))
    if c.fetchone():
        return True
    return False


def build_entry(obj, _type):
    """Insert object data into the database.
    Ignore edited objects.
    Ignore existing id's
    Determine if selfpost or a link.
    Try to insert into db 5 times in case it is locked."""
    if obj.edited:
        return None
    _id = obj.id
    _auth = obj.author.name
    if _type == 0 and not object_exists(obj):
        _self = True if obj.is_self == 1 else False
        _title = obj.title
        _link = obj.url if not _self else None
        _text = obj.selftext if obj.selftext else None
        sql = '''INSERT INTO submissions(posted, id, repost_id, self, auth, title, text, link)
        VALUES (?,?,?,?,?,?,?,?)'''
        data_tuple = (False, _id, None, _self, _auth, _title, _text, _link)
        return sql, data_tuple
    elif _type == 1 and not object_exists(obj, submission=False):
        _is_root = obj.is_root
        _text = obj.body
        _parent_id = obj.parent().id
        _sub_id = obj.submission.id
        sql = '''INSERT INTO comments (posted, id, repost_id, is_root, auth, text, parent_id, sub_id)
        VALUES (?,?,?,?,?,?,?,?)'''
        data_tuple = (False, _id, None, _is_root, _auth, _text, _parent_id, _sub_id)
        return sql, data_tuple
    else:
        return None


def store_entry(sql, data):
    tries = 0
    while tries < 5:
        try:
            c.execute(sql, data)
            conn.commit()
        except sqlite3.OperationalError as error:
            logger.exception(error)
            tries += 1
            sleep(2)
            continue
        else:
            break
    else:
        logger.error('Database Error. Update Failed.')


def fill_queue(monitored_sub, queue, obj_type):
    """Stream all submissions or comments and put them into the queue.
    Submissions are stored in a tuple with a 0, comments with a 1."""
    try:
        subreddit = reddit.subreddit(monitored_sub)
        if obj_type == 'Submission':
            for sub in subreddit.stream.submissions():
                queue.append((sub, 0))
        else:
            for com in subreddit.stream.comments():
                queue.append((com, 1))
    except Exception as error:
        logger.exception(error)
        sys.exit()


def sub_com_stream(queue):
    """Stream the comments and submissions from the queue"""
    while True:
        try:
            yield queue.pop()
        except IndexError:
            continue


def run():
    """Create a queue to use as a funnel, start the threads and dispatch as needed"""
    build_db()
    q = deque()
    s_thread = threading.Thread(target=fill_queue, args=(source, q, 'Submission'), daemon=True)
    c_thread = threading.Thread(target=fill_queue, args=(source, q, 'Comment'), daemon=True)
    s_thread.start()
    c_thread.start()
    for entry in sub_com_stream(q):
        item, kind = entry
        values = build_entry(item, kind)
        if values:
            sql, data = values
            store_entry(sql, data)


if __name__ == '__main__':
    logger.info('Start')
    run()
