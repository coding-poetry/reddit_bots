import praw

reddit = praw.Reddit('AUTHENTICATION')

auth = reddit.auth
auth.authorize(code)
auth.implicit(access_token, expires_in, scope)
auth.limits
auth.scopes()
auth.url(scopes, state, duration='permanent', implicit=False)
