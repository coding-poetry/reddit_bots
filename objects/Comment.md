# Comment Class

```python
import praw
reddit = praw.Reddit('AUTHENTICATION')

comment = reddit.comment(comment_id)
```

### Attributes

```python
comment.approved
comment.approved_by
comment.archived
comment.author_flair_css_class
comment.author_flair_text
comment.banned_by
comment.body
comment.body_html
comment.can_gild
comment.controversiality
comment.created
comment.created_utc
comment.distinguished
comment.downs
comment.edited
comment.fullname
comment.gilded
comment.id
comment.ignore_reports
comment.is_root
comment.likes
comment.link_id
comment.mod_reports
comment.name
comment.num_reports
comment.parent_id
comment.removal_reason
comment.removed
comment.report_reasons
comment.saved
comment.score
comment.score_hidden
comment.spam
comment.stickied
comment.subreddit_id
comment.subreddit_name_prefixed
comment.subreddit_type
comment.ups
comment.user_reports
```

### Functions

```python
comment.block()
comment.clear_vote()
comment.delete()
comment.downvote()
comment.edit(body)
comment.gild()
comment.mark_read()
comment.mark_unread()
comment.parent()
comment.parse(data, reddit)
comment.permalink(fast=False)
comment.refresh()
comment.reply(body)
comment.report(reason)
comment.save(category=None)
comment.unsave()
comment.upvote()
```

### Classes

#### [Author](https://github.com/kimpeek/reddit_bots/blob/master/objects/Redditor.md)

#### Mod

```python
comment.mod.approve()
comment.mod.distinguish(how='yes', sticky=False)
comment.mod.ignore_reports()
comment.mod.remove(spam=False)
comment.mod.undistinguish()
comment.mod.unignore_reports()
```

#### Replies

```python
comment.replies.list()
comment.replies.replace_more(limit=32, threshold=0)
```

#### [Submission](https://github.com/kimpeek/reddit_bots/blob/master/objects/Submission.md)

#### [Subreddit](https://github.com/kimpeek/reddit_bots/blob/master/objects/Subreddit.md)
