import praw

reddit = praw.Reddit('AUTHENTICATION')

for post in reddit.user.me().hidden(limit=None):
    post.unhide()
    
