from time import time
import praw

reddit = praw.Reddit('AUTHENTICATION')
subreddit = 'all'


def main():
    start = time()
    for submission in reddit.subreddit(subreddit).stream.submissions():
        if submission.created_utc > start:
            handle(submission)


def handle(submission):
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


if __name__ == '__main__':
    main()
