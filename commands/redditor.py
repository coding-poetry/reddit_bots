import praw

reddit = praw.Reddit('AUTHENTICATION')
USERNAME = 'abc123'

redditor = reddit.redditor(USERNAME)
redditor.comments()
redditor.comments.controversial(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
redditor.comments.hot()
redditor.comments.new()
redditor.comments.top(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
redditor.controversial(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
redditor.downvoted()
redditor.friend(note=None)
redditor.friend_info()
redditor.fullname()
redditor.gild(months=1)
redditor.gilded()
redditor.gildings()
redditor.hidden()
redditor.hot()
redditor.message(subject, message, from_subreddit=None)
redditor.multireddits()
redditor.name()
redditor.new()
redditor.saved()
redditor.submissions()
redditor.submissions.controversial(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
redditor.submissions.hot()
redditor.submissions.new()
redditor.submissions.top(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
redditor.top(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
redditor.unblock()
redditor.unfriend()
redditor.upvoted()
