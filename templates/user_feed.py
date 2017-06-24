from time import time
import praw

start = time()
reddit = praw.Reddit('AUTHENTICATION')
user = 'spez'


def handle(comment):
    print(comment.body)


def main():    
    for comment in reddit.redditor(user).comments.new(limit=None):
        if comment.created_utc > start:
            handle(comment)


if __name__ == '__main__':
    main()
