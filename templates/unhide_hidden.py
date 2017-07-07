import praw

reddit = praw.Reddit('AUTHENTICATION')

while True:
    objects = [post for post in reddit.user.me().hidden(limit=None)]
    try:
        first = objects[0]
    except IndexError:
        break
    else:
        # Reddit returns a 400 response if you try to unhide more than 40 at a time
        first.unhide(other_submissions=objects[1:40])
