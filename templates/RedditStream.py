import threading
from collections import deque


class Stream:
    """An iterator that yielda submissions and comments"""

    def __init__(self, reddit, subreddit):
        self._reddit = reddit
        self._subreddit = subreddit
        self._queue = deque()
        self._subreddit_stream()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return self._queue.pop()
            except IndexError:
                continue

    def _queue_submissions(self):
        """Stream all submissions and put them into the queue"""

        _subreddit = self._reddit.subreddit(self._subreddit)
        while True:
            try:
                for submission in _subreddit.stream.submissions():
                    self._queue.append((submission, False))
            except Exception as e:
                pass

    def _queue_comments(self):
        """Stream all comments and put them into the queue"""

        _subreddit = self._reddit.subreddit(self._subreddit)
        while True:
            try:
                for comment in _subreddit.stream.comments():
                    self._queue.append((False, comment))
            except Exception as e:
                pass

    def _subreddit_stream(self):
        """Create a queue to use as a funnel, start the threads and yield the objects"""

        submission_thread = threading.Thread(target=self._queue_submissions)
        comment_thread = threading.Thread(target=self._queue_comments)
        submission_thread.start()
        comment_thread.start()
