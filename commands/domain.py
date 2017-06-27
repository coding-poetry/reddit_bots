import praw

reddit = praw.Reddit('AUTHENTICATION')
DOMAIN_NAME = 'site.com'

domain = reddit.domain(DOMAIN_NAME)
domain.controversial(time_filter='all')  # all, day, hour, month, week, year
domain.hot()
domain.new()
domain.random_rising()
domain.rising()
domain.top(time_filter='all')  # all, day, hour, month, week, year
