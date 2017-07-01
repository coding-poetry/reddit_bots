# User Class

```python
import praw
reddit = praw.Reddit('AUTHENTICATION')

user = reddit.user
```

### Functions

```python
user.blocked()
user.contributor_subreddits()
user.friends()
user.karma()
user.me(use_cache=True)
user.moderator_subreddits()
user.multireddits()
user.subreddits()
```
