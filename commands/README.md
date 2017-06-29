### Boilerplate - [Praw.ini](https://github.com/kimpeek/reddit_bots/blob/master/templates/praw.ini)

```python
import praw
reddit = praw.Reddit('AUTHENTICATION')
```

---

### Subreddit

```python
subreddit = reddit.subreddit(SUBREDDIT_NAME)

for moderator in subreddit.moderator():
```

### Submission

---

### Comments - [Attributes](https://github.com/kimpeek/reddit_bots/blob/master/commands/comment.py)

#### Live stream
```python
for comment in reddit.subreddit(SUBREDDIT_NAME).stream.comments():
```

#### Past Comments
```python
for comment in reddit.subreddit(SUBREDDIT_NAME).comments():
    handle(comment)
```

#### Individual Comment
```python
comment = reddit.comment(COMMENT_ID)
```

### Inbox

### Redditor
