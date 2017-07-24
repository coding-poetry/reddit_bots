import time
import threading
from collections import deque
from prawcore.exceptions import PrawcoreException


class Stream:
    """A generator class of submissions and comments"""

    def __init__(self, reddit, subreddit):
        self.reddit = reddit
        self.subreddit = subreddit
        self.queue = deque()
        self.startup()

    def queue_submissions(self):
        """Stream all submissions and put them into the queue"""

        sub = self.reddit.subreddit(self.subreddit)
        while True:
            start = time.time()  # Avoid old data
            try:
                for submission in sub.stream.submissions():
                    if submission.created_utc <= start:
                        continue
                    self.queue.append((submission, False))
            except PrawcoreException:
                pass

    def queue_comments(self):
        """Stream all comments and put them into the queue"""

        sub = self.reddit.subreddit(self.subreddit)
        while True:
            start = time.time()  # Avoid old data
            try:
                for comment in sub.stream.comments():
                    if comment.created_utc <= start:
                        continue
                    self.queue.append((False, comment))
            except PrawcoreException:
                pass

    def startup(self):
        """Create a queue to use as a funnel, start the threads and puts the objects into the queue"""

        submission_thread = threading.Thread(target=self.queue_submissions)
        comment_thread = threading.Thread(target=self.queue_comments)
        submission_thread.start()
        comment_thread.start()

    def dual_stream(self):
        while True:
            try:
                yield self.queue.pop()
            except IndexError:
                continue
