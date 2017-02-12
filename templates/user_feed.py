from time import time
import praw

start = time()
reddit = praw.Reddit(
    client_id='client_id',
    client_secret='client_secret',
    password='password',
    user_agent='user_agent',
    username='username'
)


def handle(comment):
    """Disposition comments as needed"""
    
    # comment.reply('I see you!')
    print(comment.body)


def main():
    """Stream new comments made after the bot has began running.
    Past comments will be ignored"""
    
    for comment in reddit.redditor('spez').comments.new(limit=None):
        if not comment.created_utc < start:
            handle(comment)


if __name__ == '__main__':
    main()
