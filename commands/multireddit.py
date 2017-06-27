import praw

reddit = praw.Reddit('AUTHENTICATION')

multireddit = reddit.multireddit('subreddit', 'subreddit')
reddit.multireddit.create(display_name, subreddits, description_md=None, icon_name=None, key_color=None, visibility='private', weighting_scheme='classic')
multireddit.add(subreddit)
multireddit.comments()
multireddit.comments.gilded()
multireddit.controversial(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
multireddit.copy(display_name=None)
multireddit.delete()
multireddit.fullname()
multireddit.gilded()
multireddit.hot()
multireddit.name()
multireddit.new()
multireddit.path()
multireddit.random_rising()
multireddit.remove(subreddit)
multireddit.rename(display_name)
multireddit.rising()
multireddit.sluggify(title)
multireddit.top(time_filter='all')  # 'all', 'day', 'hour', 'month', 'week', 'year'
multireddit.update(**updated_settings)
