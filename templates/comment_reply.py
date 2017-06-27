import praw

reddit = praw.Reddit('AUTHENTICATION')

for reply in reddit.inbox.comment_replies():
    print(reply.author.name)
