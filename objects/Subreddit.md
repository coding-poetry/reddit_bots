# Subreddit Class

```python
import praw
reddit = praw.Reddit('AUTHENTICATION')

subreddit = reddit.subreddit(subreddit_name)
```

### Attributes

```python
subreddit.accounts_active
subreddit.accounts_active_is_fuzzed
subreddit.active_user_count
subreddit.advertiser_category
subreddit.allow_images
subreddit.banner_img
subreddit.banner_size
subreddit.collapse_deleted_comments
subreddit.comment_score_hide_mins
subreddit.created
subreddit.created_utc
subreddit.description
subreddit.description_html
subreddit.display_name
subreddit.display_name_prefixed
subreddit.fullname
subreddit.header_img
subreddit.header_size
subreddit.header_title
subreddit.hide_ads
subreddit.icon_img
subreddit.icon_size
subreddit.id
subreddit.key_color
subreddit.lang
subreddit.name
subreddit.over18
subreddit.public_description
subreddit.public_description_html
subreddit.public_traffic
subreddit.quarantine
subreddit.show_media
subreddit.show_media_preview
subreddit.spoilers_enabled
subreddit.submission_type
subreddit.submit_link_label
subreddit.submit_text
subreddit.submit_text_html
subreddit.submit_text_label
subreddit.subreddit_type
subreddit.subscribers
subreddit.suggested_comment_sort
subreddit.title
subreddit.url
subreddit.user_is_banned
subreddit.user_is_contributor
subreddit.user_is_moderator
subreddit.user_is_muted
subreddit.user_is_subscriber
subreddit.user_sr_theme_enabled
subreddit.whitelist_status
subreddit.wiki_enabled
```

### Functions

```python
subreddit.controversial(time_filter='all')  # all, day, hour, month, week, year
subreddit.gilded()
subreddit.hot()
subreddit.message(subject, message, from_subreddit=None)
subreddit.new()
subreddit.random()
subreddit.random_rising()
subreddit.rising()
subreddit.rules()
subreddit.search(query, sort='relevance', syntax='cloudsearch', time_filter='all')
subreddit.sticky(number=1)
subreddit.submissions(start=None, end=None, extra_query=None)
subreddit.submit(title, selftext=None, url=None, resubmit=True, send_replies=True)
subreddit.subscribe(other_subreddits=None)
subreddit.top(time_filter='all')  # all, day, hour, month, week, year
subreddit.traffic()
subreddit.unsubscribe(other_subreddits=None)
```

### Classes

#### Banned

```python
subreddit.banned.add(redditor)
subreddit.banned.relationship
subreddit.banned.remove(redditor)
```

#### Comments

```python
subreddit.comments.gilded()
subreddit.comments.parse(data, reddit)
```

#### Contributor

```python
subreddit.contributor.add(redditor)
subreddit.contributor.leave()
subreddit.contributor.relationship
subreddit.contributor.remove(redditor)
```

#### Filters

```python
subreddit.filters.add(subreddit)
subreddit.filters.remove(subreddit)
```

#### Flair

```python
subreddit.flair.configure(position='right', self_assign=False, link_position='left', link_self_assign=False)
subreddit.flair.delete(redditor)
subreddit.flair.delete_all()
subreddit.flair.set(redditor=None, text='', css_class='', thing=None)
subreddit.flair.templates.add(text, css_class='', text_editable=False, is_link=False)
subreddit.flair.templates.clear(is_link=False)
subreddit.flair.templates.delete(template_id)
subreddit.flair.templates.flair_type(is_link)
subreddit.flair.templates.update(template_id, text, css_class='', text_editable=False)
subreddit.flair.update(flair_list, text='', css_class='')
```

#### Mod

```python
subreddit.mod.accept_invite()
subreddit.mod.approve(thing)  # DEPRICATED
subreddit.mod.distinguish(thing, how='yes', sticky=False)  # DEPRICATED
subreddit.mod.edited(only=None)
subreddit.mod.ignore_reports(thing)  # DEPRICATED
subreddit.mod.inbox()
subreddit.mod.log(action=None, mod=None)
subreddit.mod.modqueue(only=None)
subreddit.mod.remove(thing, spam=False)  # DEPRICATED
subreddit.mod.reports(only=None)
subreddit.mod.settings()
subreddit.mod.spam(only=None)
subreddit.mod.undistinguish(thing)  # DEPRICATED
subreddit.mod.unignore_reports(thing)  # DEPRICATED
subreddit.mod.unmoderated()
subreddit.mod.unread()
subreddit.mod.update()  # See help(subreddit.mod.update) to see extensive list of params
```

#### Moderator

```python
subreddit.moderator.add(redditor, permissions=None)
subreddit.moderator.invite(redditor, permissions=None)
subreddit.moderator.leave()
subreddit.moderator.relationship
subreddit.moderator.remove(redditor)
subreddit.moderator.remove_invite(redditor)
subreddit.moderator.update(redditor, permissions=None)
subreddit.moderator.update_invite(redditor, permissions=None)
```

#### Modmail

```python
subreddit.modmail.bulk_read(other_subreddits=None, state=None)
subreddit.modmail.conversations(after=None, limit=None, other_subreddits=None, sort=None, state=None)
subreddit.modmail.create(subject, body, recipient, author_hidden=False)
subreddit.modmail.subreddits()
subreddit.modmail.unread_count()
```

#### Muted

```python
subreddit.muted.add(redditor)
subreddit.muted.relationship
subreddit.muted.remove(redditor)
```

#### Quaran

```python
subreddit.quaran.opt_in()
subreddit.quaran.opt_out()
```

#### Stream

```python
subreddit.stream.comments()
subreddit.stream.submissions()
```

#### Stylesheet

```python
subreddit.stylesheet.delete_header()
subreddit.stylesheet.delete_image(name)
subreddit.stylesheet.delete_mobile_header()
subreddit.stylesheet.delete_mobile_icon()
subreddit.stylesheet.update(stylesheet, reason=None)
subreddit.stylesheet.upload(name, image_path)
subreddit.stylesheet.upload_header(image_path)
subreddit.stylesheet.upload_mobile_header(image_path)
subreddit.stylesheet.upload_mobile_icon(image_path)
```

#### Wiki

```python
subreddit.wiki.banned.add()
subreddit.wiki.banned.relationship
subreddit.wiki.banned.remove()
subreddit.wiki.contributor.add()
subreddit.wiki.contributor.relationship
subreddit.wiki.contributor.remove()
subreddit.wiki.create(name, content, reason=None, **other_settings)
subreddit.wiki.revisions()
```
