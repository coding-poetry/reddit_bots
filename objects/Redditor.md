# Redditor Class

```python
import praw
reddit = praw.Reddit('AUTHENTICATION')

redditor = reddit.redditor(username)
```

### Attributes

```python
redditor.fullname
```

### Functions

```python
redditor.controversial(time_filter='all')  # all, day, hour, month, week, year
redditor.downvoted()
redditor.friend(note=None)
redditor.friend_info()
redditor.from_data(reddit, data)
redditor.gild(months=1)
redditor.gilded()
redditor.gildings()
redditor.hidden()
redditor.hot()
redditor.message(subject, message, from_subreddit=None)
redditor.multireddits()
redditor.name()
redditor.new()
redditor.parse()
redditor.saved()
redditor.top(time_filter='all')  # all, day, hour, month, week, year
redditor.unblock()
redditor.unfriend()
redditor.upvoted()
```

### Classes
```python
redditor.comments
redditor.submissions
```
