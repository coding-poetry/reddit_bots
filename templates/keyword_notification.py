from time import time
import praw

selected_sub = 'all'
start = time()
reddit = praw.Reddit('AUTHENTICATION')


def handle(comment):
    keywords = ['kitten', 'cat', 'kitty']
    if any(keyword in comment.body for keyword in keywords):
        link = 'http://www.reddit.com{}'.format(comment.permalink())
        reddit.redditor('username').message('Keyword Mentioned', link)


def main():
    comment_stream = reddit.subreddit(sub).stream.comments()
    for comment in comment_stream:
        if comment.created_utc > start:
            handle(comment)

if __name__ == '__main__':
    main()
