from time import time
import praw
from RedditStream import Stream

reddit = praw.Reddit('AUTHENTICATION')
subreddit = 'all'


def main():
    for item in Stream(reddit, subreddit).dual_stream():
        submission, comment = item
        if submission:
            handle_submission(submission)
        else:
            handle_comment(comment)


def handle_submission(submission):
    _id = submission.id
    url = submission.url if not submission.is_self else None
    title = submission.title
    selftext = submission.selftext if submission.is_self else None
    permalink = 'http://www.reddit.com{}'.format(submission.permalink)
    shortlink = submission.shortlink
    created_utc = submission.created_utc

    author = submission.author
    verified = submission.author.verified
    author_age = submission.author.created_utc
    link_karma = submission.author.link_karma
    comment_karma = submission.author.comment_karma

    submission.author.friend(note=None)
    submission.reply(body)
    submission.report(reason)
    submission.author.message(subject, message, from_subreddit=None)

    submission.mod.approve()
    submission.mod.distinguish(how='yes', sticky=False)  # yes, no, admin, special
    submission.mod.ignore_reports()
    submission.mod.remove(spam=False)
    submission.mod.sticky(state=True, bottom=True)


def handle_comment(comment):
    _id = comment.id
    body = comment.body
    is_root = comment.is_root
    parent_id = comment.parent_id
    created_utc = comment.created_utc
    author_flair_text = comment.author_flair_text
    author_flair_css_class = comment.author_flair_css_class

    parent = comment.parent()
    permalink = comment.permalink(fast=False)

    author = comment.author
    verified = comment.author.verified
    author_age = comment.author.created_utc
    link_karma = comment.author.link_karma
    comment_karma = comment.author.comment_karma

    comment.author.friend(note=None)
    comment.reply(body)
    comment.report(reason)
    comment.author.message(subject, message, from_subreddit=None)

    comment.reply(body)
    comment.report(reason)

    comment.mod.approve()
    comment.mod.distinguish(how='yes', sticky=False)
    comment.mod.ignore_reports()
    comment.mod.remove(spam=False)


if __name__ == '__main__':
    main()
