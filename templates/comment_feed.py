from time import time
import praw

reddit = praw.Reddit('AUTHENTICATION')
subreddit = 'all'


def main():
    start = time()
    for comment in reddit.subreddit(subreddit).stream.comments():
        if comment.created_utc > start:
            handle(comment)


def handle(comment):
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
