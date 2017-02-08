from time import sleep, strftime, time
import configparser
import prawcore
import logging
import praw
from collections import deque
import threading
import sqlite3

start = time()
config = configparser.ConfigParser()
config.read('bot.conf', encoding='utf-8')
AUTH = config['AUTHENTICATION']
LOG = config['LOGGING']
REDDIT = config['REDDIT']
source = REDDIT['src']
DB = config['DATABASE']
database = DB['db_file']
logging.basicConfig(filename=LOG['log_file'], level=logging.WARNING, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)
reddit = praw.Reddit(
    password=AUTH['password'],
    username=AUTH['username'],
    client_id=AUTH['client_id'],
    user_agent=AUTH['user_agent'],
    client_secret=AUTH['client_secret'])
conn = sqlite3.connect(database)
c = conn.cursor()

logger.disabled = False
max_restarts = 1
wait = 1


def handle_submission(submission):
    # Load into submissions DB table
    """
    Deliver the desired content however you need.
    See comment block above for available methods
    and attributes on the submission object

    Example:

    print(submission.author)

    :param submission: PRAW submission object
    :return: None
    """
    """
    from pprint import pprint
    pprint(dir(submission))

    ['STR_FIELD',
     '__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattr__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     '_comments_by_id',
     '_fetch',
     '_fetched',
     '_flair',
     '_info_path',
     '_mod',
     '_reddit',
     '_reset_attributes',
     '_safely_add_arguments',
     '_vote',
     'approved_by',
     'archived',
     'author',
     'author_flair_css_class',
     'author_flair_text',
     'banned_by',
     'clear_vote',
     'clicked',
     'comment_limit',
     'comment_sort',
     'comments',
     'contest_mode',
     'created',
     'created_utc',
     'delete',
     'distinguished',
     'domain',
     'downs',
     'downvote',
     'duplicates',
     'edit',
     'edited',
     'flair',
     'fullname',
     'gild',
     'gilded',
     'hidden',
     'hide',
     'hide_score',
     'id',
     'id_from_url',
     'is_self',
     'likes',
     'link_flair_css_class',
     'link_flair_text',
     'locked',
     'media',
     'media_embed',
     'mod',
     'mod_reports',
     'name',
     'num_comments',
     'num_reports',
     'over_18',
     'parse',
     'permalink',
     'post_hint',
     'preview',
     'quarantine',
     'removal_reason',
     'reply',
     'report',
     'report_reasons',
     'save',
     'saved',
     'score',
     'secure_media',
     'secure_media_embed',
     'selftext',
     'selftext_html',
     'shortlink',
     'spoiler',
     'stickied',
     'subreddit',
     'subreddit_id',
     'suggested_sort',
     'thumbnail',
     'title',
     'unhide',
     'unsave',
     'ups',
     'upvote',
     'url',
     'user_reports',
     'visited']
    """
    _author = submission.author.name
    _id = submission.id
    _time = submission.created_utc
    _title = submission.title
    _url = submission.url
    _text = submission.selftext
    print('Submission', submission.author.name)


def handle_comment(comment):
    # Load into comments DB table
    """
    Deliver the desired content however you need.
    See comment block above for available methods
    and attributes on the comment object

    Example:

    print(comment.author)

    :param comment: PRAW comment object
    :return: None
    """
    """
    from pprint import pprint
    pprint(dir(comment))

    ['STR_FIELD',
     '__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattr__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     '_fetch',
     '_fetched',
     '_mod',
     '_reddit',
     '_replies',
     '_reset_attributes',
     '_safely_add_arguments',
     '_submission',
     '_vote',
     'approved_by',
     'archived',
     'author',
     'author_flair_css_class',
     'author_flair_text',
     'banned_by',
     'block',
     'body',
     'body_html',
     'clear_vote',
     'controversiality',
     'created',
     'created_utc',
     'delete',
     'distinguished',
     'downs',
     'downvote',
     'edit',
     'edited',
     'fullname',
     'gild',
     'gilded',
     'id',
     'is_root',
     'likes',
     'link_author',
     'link_id',
     'link_title',
     'link_url',
     'mark_read',
     'mark_unread',
     'mod',
     'mod_reports',
     'name',
     'num_reports',
     'over_18',
     'parent',
     'parent_id',
     'parse',
     'permalink',
     'quarantine',
     'refresh',
     'removal_reason',
     'replies',
     'reply',
     'report',
     'report_reasons',
     'save',
     'saved',
     'score',
     'score_hidden',
     'stickied',
     'submission',
     'subreddit',
     'subreddit_id',
     'unsave',
     'ups',
     'upvote',
     'user_reports']
    """
    print('Comment', comment.author.name)


def _feed_subs_to_queue(monitored_sub, queue):
    """Stream all submissions and put them into the queue.
    Submissions are stored in a tuple with a 0.
    Error logging should be established as needed."""

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
    Comments are stored in a tuple with a 1.
    Error logging should be established as needed."""

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
    s_thread = threading.Thread(target=_feed_subs_to_queue, args=(source, q))
    c_thread = threading.Thread(target=_feed_comms_to_queue, args=(source, q))
    s_thread.start()
    c_thread.start()
    for entry in sub_com_stream(q):
        if entry[1] == 0:
            handle_submission(entry[0])
        else:
            handle_comment(entry[0])


if __name__ == '__main__':
    restarts = 0
    while restarts < max_restarts:
        try:
            main()
        except prawcore.exceptions.OAuthException as e:
            logger.exception(e)
            break
        except prawcore.exceptions.RequestException as e:
            logger.exception(e)
            restarts += 1
            sleep(wait)
            continue
        except prawcore.exceptions.ResponseException as e:
            logger.exception(e)
            restarts += 1
            sleep(wait)
            continue
        except Exception as e:
            logger.exception(e)
            restarts += 1
            sleep(wait)
            continue
        else:
            logger.error('Max restarts exceeded')
    logger.error('Stop')
