from time import sleep, strftime
import sqlite3
import praw

log_file = 'req_bot_log.txt'
conn = sqlite3.connect('bdb_pa_FoxK56.db')
c = conn.cursor()

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    password='',
    user_agent='Linux:borrow_limiter:0.1 (by /u/Foxk56)',
    username=''
)


def build_db():
    """Create a 3-column database table if it doesn't exist"""

    c.execute("""CREATE TABLE IF NOT EXISTS bph(auth TEXT, time TEXT, id TEXT)""")
    conn.commit()


def monitor():
    """Stream new submissions to /r/borrow and evaluate each
    If the bot experiences an error, notify the owner and attempt to restart every 10 minutes.
    If unable to restart after 5 attempts, stop the bot"""

    notified = False
    restart = 0
    while restart < 200:
        try:
            subreddit = reddit.subreddit('borrow')
            submission_stream = subreddit.stream.submissions()
            for submission in submission_stream:
                if '[req]' in str(submission.title).lower():
                    evaluate(submission)
        except Exception as e:
            log_event('Reset\t\t{}: {}'.format(type(e).__name__, e))
            if not notified:
                msg = 'Your bot experienced a terminal error and is attempting to restart.' \
                      'Please manually restart the bot to ensure a clean restart.'
                reddit.redditor('Foxk56').message('BOT ERROR', msg)
                notified = True
            sleep(600)
            restart += 1
            continue
    log_event('Stopped\t\tExcessive Restarts\n')


def log_event(string):
    """Log events and errors"""

    with open(log_file, 'a') as log:
        log.write('{}\t\t'.format(strftime("%Y-%m-%d\t%H:%M:%S")) + string + '\n')


def evaluate(sub):
    """Compare this sub's time with previous time and disposition"""

    prev_auth, prev_time, prev_id = get_last(sub.author.name)
    if prev_auth:
        if sub.id != prev_id and sub.created_utc - float(prev_time) < 86400:
            notify(sub)
        else:
            update_author(sub)
    else:
        new_author(sub)


def get_last(author):
    """Get the last post by this author. If no history, return 0"""

    # (author, time, id)
    c.execute("""SELECT * FROM bph WHERE auth=(?)""", (author,))
    entries = [row for row in c.fetchall()]
    if entries:
        return entries[0]
    return None, 0, None


def notify(sub):
    """Report previous post made < 24hrs ago"""

    reason = """Redditor has made a [REQ] less than 24 hours ago"""
    sub.report(reason)


def update_author(sub):
    """Find last post by author and update time/id"""

    c.execute("""UPDATE bph SET time=(?), id=(?)
    WHERE auth=(?)""", (sub.created_utc, sub.id, sub.author.name))
    conn.commit()


def new_author(sub):
    """Create an entry for the author"""

    c.execute("""INSERT INTO bph(auth, time, id)
    VALUES (?,?,?)""", (sub.author.name, sub.created_utc, sub.id))
    conn.commit()

if __name__ == '__main__':
    log_event('Start')
    build_db()
    monitor()
