import praw

reddit = praw.Reddit('AUTHENTICATION')

subreddits = reddit.subreddits
subreddits.default()
subreddits.gold()
subreddits.new()
subreddits.popular()
subreddits.recommended(subreddits, omit_subreddits=None)
subreddits.search()
subreddits.search_by_name(query, include_nsfw=True, exact=Fals)
subreddits.search_by_topic(query)
subreddits.stream(**stream_options)
