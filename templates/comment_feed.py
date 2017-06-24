from time import time
import praw

sub = 'all'
start = time()
reddit = praw.Reddit('AUTHENTICATION')


def handle(comment):
    pass


def main():
    comment_stream = reddit.subreddit(sub).stream.comments()
    for comment in comment_stream:
        if comment.created_utc < start:
            continue
        handle(comment)

if __name__ == '__main__':
    main()
