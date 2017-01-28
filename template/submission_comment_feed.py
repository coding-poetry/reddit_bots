from time import time
import threading
from collections import deque
import praw

selected_sub = 'all'
start = time()
reddit = praw.Reddit(
    client_id='client_id',
    client_secret='client_secret',
    password='password',
    user_agent='user_agent',
    username='username'
)


def handle_submission(submission):
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
    pass


def handle_comment(comment):
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
    pass


def _feed_subs_to_queue(monitored_sub, queue):
    """Stream all submissions and put them into the queue.
    Submissions are stored in a tuple with a 0.
    Error logging should be established as needed."""

    subreddit = reddit.subreddit(monitored_sub)
    while True:
        try:
            for sub in subreddit.stream.submissions():
                queue.append((sub, 0))
        except Exception as e:
            print('Submission stream error. Resetting')
            print(e)
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
        except Exception as e:
            print('Comment stream error. Resetting')
            print(e)
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
    s_thread = threading.Thread(target=_feed_subs_to_queue, args=(selected_sub, q))
    c_thread = threading.Thread(target=_feed_comms_to_queue, args=(selected_sub, q))
    s_thread.start()
    c_thread.start()
    for entry in sub_com_stream(q):
        if entry[1] == 0:
            handle_submission(entry[0])
        else:
            handle_comment(entry[0])


if __name__ == '__main__':
    main()
