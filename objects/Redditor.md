# Redditor Class

```python
import praw
reddit = praw.Reddit('AUTHENTICATION')

redditor = reddit.redditor(username)
```

### Attributes

```python
redditor.comment_karma
redditor.created
redditor.created_utc
redditor.fullname
redditor.has_subscribed
redditor.has_verified_email
redditor.hide_from_robots
redditor.id
redditor.is_employee
redditor.is_friend
redditor.is_gold
redditor.is_mod
redditor.link_karma
redditor.name
redditor.pref_show_snoovatar
redditor.subreddit  # Currently a dict for profile users. May be treated as a subreddit in the future
redditor.upvoted
redditor.verified
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
redditor.parse(data, reddit)
redditor.saved()
redditor.top(time_filter='all')  # all, day, hour, month, week, year
redditor.unblock()
redditor.unfriend()
redditor.upvoted()
```

### Classes

#### Comments

```python
redditor.comments
redditor.comments.controversial(time_filter='all')  # all, day, hour, month, week, year
redditor.comments.hot()
redditor.comments.new()
redditor.comments.parse(data, reddit)
redditor.comments.top(time_filter='all')  # all, day, hour, month, week, year
```

#### Submissions

```python
redditor.submissions
redditor.submissions.controversial(time_filter='all')  # all, day, hour, month, week, year
redditor.submissions.hot()
redditor.submissions.new()
redditor.submissions.parse(data, reddit)
redditor.submissions.top(time_filter='all')  # all, day, hour, month, week, year
```
