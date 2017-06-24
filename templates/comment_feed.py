from time import time
import praw

sub = 'all'
start = time()
reddit = praw.Reddit('AUTHENTICATION')


def handle(comment):
    print(comment.author.name)


def main():
    comment_stream = reddit.subreddit(sub).stream.comments()
    for comment in comment_stream:
        if comment.created_utc > start:
            handle(comment)

if __name__ == '__main__':
    main()
