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
user.moderator_subreddits()
user.multireddits()
user.subreddits()
```


### Classes

#### Me

```python
me = reddit.user.me(use_cache=True)

me.comment_karma
me.comments
me.controversial
me.created
me.created_utc
me.downvoted
me.features
me.friend
me.friend_info
me.from_data
me.fullname
me.gild
me.gilded
me.gildings
me.gold_creddits
me.gold_expiration
me.has_mail
me.has_mod_mail
me.has_subscribed
me.has_verified_email
me.hidden
me.hide_from_robots
me.hot
me.id
me.in_beta
me.inbox_count
me.is_employee
me.is_gold
me.is_mod
me.is_sponsor
me.is_suspended
me.link_karma
me.message
me.multireddits
me.name
me.new
me.new_modmail_exists
me.oauth_client_id
me.over_18
me.parse
me.pref_no_profanity
me.pref_show_snoovatar
me.pref_top_karma_subreddits
me.saved
me.submissions
me.subreddit
me.suspension_expiration_utc
me.top
me.unblock
me.unfriend
me.upvoted
me.verified
```
