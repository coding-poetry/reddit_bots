import praw
from RedditStream import Stream

reddit = praw.Reddit('AUTHENTICATION')
subreddit = 'all'
stream = Stream(reddit, subreddit)


def handle_submission(submission):
    print(submission.author.name)


def handle_comment(comment):
    print(comment.author.name)


def main():
    for item in stream:
        submission, comment = item
        if submission:
            handle_submission(submission)
        else:
            handle_comment(comment)

if __name__ == '__main__':
    main()
