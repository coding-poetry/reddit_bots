from time import time
import praw

user = 'username'
sub = 'subreddit'
start = time()
reddit = praw.Reddit('AUTHENTICATION')


def handle(comment):
    keywords = ['kitten', 'cat', 'kitty']
    if any(keyword in comment.body for keyword in keywords):
        link = 'http://www.reddit.com{}'.format(comment.permalink())
        reddit.redditor(user).message('Keyword Mentioned', link)


def main():
    for comment in reddit.subreddit(sub).stream.comments():
        if comment.created_utc > start:
            handle(comment)

if __name__ == '__main__':
    main()
