import praw

reddit = praw.Reddit('AUTHENTICATION')

while True:
    objects = [post for post in reddit.user.me().hidden(limit=None)]
    try:
        first = objects[0]
    except IndexError:
        break
    else:
        print('{} hidden objects remaining'.format(len(objects)))
        
        # Reddit returns a 400 http response if more than 40 objects are unhidden at a time
        first.unhide(other_submissions=objects[1:40])

print('No hidden objects remaining')
