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
inbox.sent()
inbox.stream()
inbox.submission_replies()
inbox.unread(mark_read=False)
```
---

##### `message()` and `messages()` return a [Message](https://github.com/kimpeek/reddit_bots/blob/master/objects/Message.md) object.

##### `comment_replies()`, `mentions()` and `submission_replies()` return a [Comment](https://github.com/kimpeek/reddit_bots/blob/master/objects/Comment.md) object with the additional attributes:

#### New Attributes

```
comment_reply.context
comment_reply.dest
comment_reply.first_message
comment_reply.first_message_name
comment_reply.link_title
comment_reply.new
comment_reply.num_comments
comment_reply.subject
comment_reply.was_comment
```

#### Unavailable Attributes

```python
comment.approved
comment.approved_by
comment.archived
comment.author_flair_css_class
comment.author_flair_text
comment.banned_by
comment.can_gild
comment.controversiality
comment.downs
comment.edited
comment.gilded
comment.ignore_reports
comment.link_id
comment.mod_reports
comment.num_reports
comment.removal_reason
comment.removed
comment.report_reasons
comment.saved
comment.score_hidden
comment.spam
comment.stickied
comment.subreddit_id
comment.subreddit_type
comment.ups
comment.user_reports
```
