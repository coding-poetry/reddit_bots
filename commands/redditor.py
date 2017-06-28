import praw

reddit = praw.Reddit('AUTHENTICATION')

redditor = reddit.redditor('spez')
redditor = comment.author
redditor = message.author
redditor = submission.author

redditor.comment_karma
redditor.comments()
redditor.comments.controversial(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
redditor.comments.hot()
redditor.comments.new()
redditor.comments.top(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
redditor.controversial
redditor.created
redditor.created_utc
redditor.downvoted
redditor.features
redditor.friend
redditor.friend_info
redditor.from_data
redditor.fullname
redditor.gild
redditor.gilded
redditor.gildings
redditor.gold_creddits
redditor.gold_expiration
redditor.has_mail
redditor.has_mod_mail
redditor.has_subscribed
redditor.has_verified_email
redditor.hidden
redditor.hide_from_robots
redditor.hot
redditor.id
redditor.in_beta
redditor.inbox_count
redditor.is_employee
redditor.is_friend
redditor.is_gold
redditor.is_mod
redditor.is_sponsor
redditor.is_suspended
redditor.link_karma
redditor.message
redditor.modhash
redditor.multireddits
redditor.name
redditor.new
redditor.new_modmail_exists
redditor.over_18
redditor.parse
redditor.pref_no_profanity
redditor.pref_show_snoovatar
redditor.pref_top_karma_subreddits
redditor.saved
redditor.submissions()
redditor.submissions.controversial(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
redditor.submissions.hot()
redditor.submissions.new()
redditor.submissions.top(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
redditor.subreddit
redditor.suspension_expiration_utc
redditor.top
redditor.unblock
redditor.unfriend
redditor.upvoted
redditor.verified
