from time import time
import praw

selected_sub = 'all'
start = time()
reddit = praw.Reddit(
    client_id='client_id',
    client_secret='client_secret',
    password='password',
    user_agent='user_agent',
    username='username'
)


def handle(comment):
    keywords = ['kitten', 'cat', 'kitty']
    if any(keyword in comment.body for keyword in keywords):
        link = 'http://www.reddit.com{}'.format(comment.permalink())
        reddit.redditor('username').message('Keyword Mentioned', link)


def main():
    subreddit = reddit.subreddit(selected_sub)
    comment_stream = subreddit.stream.comments()
    for comment in comment_stream:
        if comment.created_utc < start:
            continue
        handle(comment)

if __name__ == '__main__':
    main()
