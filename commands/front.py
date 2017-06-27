import praw

reddit = praw.Reddit('AUTHENTICATION')

front = reddit.front
front.comments()
front.controversial()
front.gilded()
front.hot()
front.new()
front.random_rising()
front.rising()
front.top(time_filter='all')  # all, day, hour, month, week, year
