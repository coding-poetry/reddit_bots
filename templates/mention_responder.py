import praw

reddit = praw.Reddit('AUTHENTICATION')


def main():
    for mention in reddit.inbox.mentions():
        handle(mention)


def handle(mention):
    _id = mention.id
    body = mention.body
    is_root = mention.is_root
    parent_id = mention.parent_id
    created_utc = mention.created_utc
    was_comment = mention.was_comment

    parent = mention.parent()
    permalink = mention.permalink(fast=False)

    author = mention.author
    verified = mention.author.verified
    author_age = mention.author.created_utc
    link_karma = mention.author.link_karma
    comment_karma = mention.author.comment_karma

    mention.author.friend(note=None)
    mention.reply(body)
    mention.report(reason)
    mention.author.message(subject, message, from_subreddit=None)

    mention.reply(body)
    mention.report(reason)

    mention.mod.approve()
    mention.mod.distinguish(how='yes', sticky=False)
    mention.mod.ignore_reports()
    mention.mod.remove(spam=False)
    
    mention.mark_read()


if __name__ == '__main__':
    main()
