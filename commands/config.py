import praw

reddit = praw.Reddit('AUTHENTICATION')

config = reddit.config
config.check_for_updates()
config.client_id()
config.client_secret()
config.custom()
config.http_proxy()
config.https_proxy()
config.kinds()
config.oauth_url()
config.password()
config.reddit_url()
config.redirect_uri()
config.refresh_token()
config.short_url()
config.user_agent()
config.username()
