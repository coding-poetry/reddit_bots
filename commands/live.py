import praw

reddit = praw.Reddit('AUTHENTICATION')

reddit.live.create(title, description=None, nsfw=False, resources=None)
reddit.live.info(ids)
reddit.live.now()

live = reddit.live('ukaeu1ik4sw5')
live.contrib()
live.contributor()
live.discussions()
live.fullname()
live.id()
live.report()
live.updates()
