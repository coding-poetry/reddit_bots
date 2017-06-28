import praw

reddit = praw.Reddit('AUTHENTICATION')

comment_stream = reddit.subreddit(subreddit).stream.comments()
comments = reddit.subreddit(subreddit).comments()
comment = reddit.comment(comment_id)

submission_stream = reddit.subreddit(subreddit).stream.submissions()
submissons = reddit.subreddit(subreddit).submissions()
submission = reddit.submission(submission_id)

subreddit = reddit.subreddit(subreddit)

inbox = reddit.inbox
inbox.all()
inbox.comment_replies()
inbox.mentions()
inbox.messages()
inbox.sent()
inbox.submission_replies()
inbox.unread()

moderators = reddit.subreddit(subreddit).moderator()

redditor = reddit.redditor(username)

# Send Message
redditor.message(subject, message)

# Post Comment

# Submit Selfpost

# Submit Link

# Reply to Comment

# Reply to Submission

# Distinguish

# Sticky a Comment

# Sticky a Submission

# Set User Flair

# Set Submission Flair

# Update Wiki

# Update Sidebar
