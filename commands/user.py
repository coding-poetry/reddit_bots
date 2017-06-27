import praw

reddit = praw.Reddit('AUTHENTICATION')

user = reddit.user
user.blocked()
user.contributor_subreddits()
user.friends()
user.karma()
user.me(use_cache=True)
user.moderator_subreddits()
user.multireddits()
user.subreddits()
