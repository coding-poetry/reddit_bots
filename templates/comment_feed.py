from time import time
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


def handle(comment):
    """
    Deliver the desired content however you need.
    See comment block above for available methods
    and attributes on the comment object

    Example:

    print(comment.author)

    :param comment: PRAW comment object
    :return: None
    """
    pass


def main():
    subreddit = reddit.subreddit(selected_sub)
    comment_stream = subreddit.stream.comments()
    for comment in comment_stream:
        if comment.created_utc < start:
            continue
        handle(comment)

if __name__ == '__main__':
    main()
