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


def handle(submission):
    """
    Deliver the desired content however you need.
    See comment block above for available methods
    and attributes on the submission object

    Example:

    print(submission.author)

    :param submission: PRAW submission object
    :return: None
    """
    pass


def main():
    subreddit = reddit.subreddit(selected_sub)
    submission_stream = subreddit.stream.submissions()
    for submission in submission_stream:
        if submission.created_utc < start:
            continue
        handle(submission)


if __name__ == '__main__':
    main()
