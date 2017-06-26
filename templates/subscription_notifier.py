from time import time
import praw

user = 'username'
sub = 'subreddit'
start = time()
reddit = praw.Reddit('AUTHENTICATION')


def handle(submission):
    link = 'https://www.reddit.com{}'.format(submission.permalink)
    body = "[{}]({})".format(submission.title, link)
    reddit.redditor(user).message("New submission", body)


def main():
    submission_stream = reddit.subreddit(sub).stream.submissions()
    for submission in submission_stream:
        if submission.created_utc > start:
            handle(submission)

if __name__ == '__main__':
    main()
