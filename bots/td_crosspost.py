from time import time, strftime, sleep
import praw

source = 'the_donald'
dest = 'td_uncensored'
log_file = 'td_bot_log.txt'

reddit = praw.Reddit(
    client_id='client_id',
    client_secret='client_secret',
    password='password',
    username='username',
    user_agent='linux:td_uncensored:0.1 (by /u/username)'
)


def log_event(string):
    """Log events and errors"""

    with open(log_file, 'a') as log:
        log.write('{}\t\t'.format(strftime("%Y-%m-%d\t%H:%M:%S")) + string + '\n')


def cross_post(sub):
    """Create the cross-post"""

    if sub.selftext:
        reddit.subreddit(dest).submit(title=sub.title, selftext=sub.selftext, send_replies=False)
        return
    reddit.subreddit(dest).submit(title=sub.title, url=sub.url, send_replies=False)


def main():
    """Stream and cross-post submissions. Exit if more than 5 restarts"""

    resets = 0
    while resets < 5:
        start = time()
        try:
            for submission in reddit.subreddit(source).stream.submissions():
                if not submission.created_utc < start:
                    cross_post(submission)
        except Exception as e:
            log_event('Reset\t\t{}: {}'.format(type(e).__name__, e))
            resets += 1
            sleep(60)
            continue
    log_event('Stopped\t\tExcessive Restarts\n')

if __name__ == '__main__':
    log_event('Start')
    main()
