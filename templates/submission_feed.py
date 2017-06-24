from time import time
import praw

sub = 'all'
start = time()
reddit = praw.Reddit('AUTHENTICATION')


def handle(submission):
    print(submission.author.name)


def main():
    submission_stream = reddit.subreddit(sub).stream.submissions()
    for submission in submission_stream:
        if submission.created_utc < start:
            continue
        handle(submission)

if __name__ == '__main__':
    main()
