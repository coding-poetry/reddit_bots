# Inbox Class

```python
import praw
reddit = praw.Reddit('AUTHENTICATION')

inbox = reddit.inbox
```

### Functions

```python
inbox.all()
inbox.comment_replies()
inbox.mark_read(items)
inbox.mark_unread(items)
inbox.mentions()
inbox.message(message_id)
inbox.messages()
inbox.parse(data, reddit)
inbox.sent()
inbox.stream()
inbox.submission_replies()
inbox.unread(mark_read=False)
```
