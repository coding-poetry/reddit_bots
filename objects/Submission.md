# Submission Class

```python
import praw
reddit = praw.Reddit('AUTHENTICATION')

submission = reddit.submission(submission_id)
```

### Attributes

```python
submission.approved_by
submission.archived
submission.author_flair_css_class
submission.author_flair_text
submission.banned_by
submission.brand_safe
submission.can_gild
submission.clicked
submission.comment_limit
submission.comment_sort
submission.contest_mode
submission.created
submission.created_utc
submission.distinguished
submission.domain
submission.downs
submission.edited
submission.fullname
submission.hidden
submission.hide_score
submission.id
submission.is_self
submission.is_video
submission.likes
submission.link_flair_css_class
submission.link_flair_text
submission.locked
submission.media
submission.media_embed
submission.mod_reports
submission.name
submission.num_comments
submission.num_reports
submission.over_18
submission.permalink
submission.quarantine
submission.removal_reason
submission.report_reasons
submission.saved
submission.score
submission.secure_media
submission.secure_media_embed
submission.selftext
submission.selftext_html
submission.shortlink
submission.spoiler
submission.stickied
submission.subreddit_id
submission.subreddit_name_prefixed
submission.subreddit_type
submission.suggested_sort
submission.thumbnail
submission.thumbnail_height
submission.thumbnail_width
submission.title
submission.ups
submission.upvote_ratio
submission.url
submission.user_reports
submission.view_count
submission.visited
```

### Functions

```python
submission.clear_vote()
submission.delete()
submission.duplicates()
submission.downvote()
submission.edit(body)
submission.gild()
submission.gilded()
submission.hide(other_submissions=None)
submission.id_from_url(url)
submission.parse(data, reddit)
submission.reply(body)
submission.report(reason)
submission.save(category=None)
submission.unhide(other_submissions=None)
submission.unsave()
submission.upvote()
```

### Classes

#### [Author](https://github.com/kimpeek/reddit_bots/blob/master/objects/Redditor.md)

#### Comments

```python
submission.comments.list()
submission.comments.replace_more()
```

#### Flair

```python
submission.flair.choices()
submission.flair.select(flair_template_id, text=None)
```

#### Mod

```python
submission.mod.approve()
submission.mod.contest_mode(state=True)
submission.mod.distinguish(how='yes', sticky=False)  # yes, no, admin, special
submission.mod.flair(text='', css_class='')
submission.mod.ignore_reports()
submission.mod.lock()
submission.mod.nsfw()
submission.mod.remove(spam=False)
submission.mod.sfw()
submission.mod.spoiler()
submission.mod.sticky(state=True, bottom=True)
submission.mod.suggested_sort(sort='blank')  # confidence, top, new, controversial, old, random, qa, blank (default: blank)
submission.mod.undistinguish()
submission.mod.unignore_reports()
submission.mod.unlock()
submission.mod.unspoiler()
```

#### [Subreddit](https://github.com/kimpeek/reddit_bots/blob/master/objects/Subreddit.md)
