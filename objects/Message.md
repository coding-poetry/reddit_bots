# Inbox Class

```python
import praw
reddit = praw.Reddit('AUTHENTICATION')

message = reddit.inbox.message(message_id)
```

### Attributes

```python
message.body
message.body_html
message.context
message.created
message.created_utc
message.distinguished
message.first_message
message.first_message_name
message.fullname
message.id
message.likes
message.name
message.new
message.num_comments
message.parent_id
message.replies
message.score
message.subject
message.subreddit_name_prefixed
message.was_comment
```

### Functions

```python
message.block()
message.mark_read()
message.mark_unread()
message.reply(body)
```

### Classes

#### [Author](https://github.com/kimpeek/reddit_bots/blob/master/objects/Redditor.md)

#### [Dest](https://github.com/kimpeek/reddit_bots/blob/master/objects/Redditor.md)

#### [Subreddit](https://github.com/kimpeek/reddit_bots/blob/master/objects/Subreddit.md)
