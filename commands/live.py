import praw

reddit = praw.Reddit('AUTHENTICATION')
LIVE_ID = 'abc123'

reddit.live.create(title, description=None, nsfw=False, resources=None)
reddit.live.info(ids)
reddit.live.now()

live = reddit.live(LIVE_ID)
live.contrib()
live.contrib.add(body)
live.contrib.close()
live.contrib.thread()
live.contrib.update(title=None, description=None, nsfw=None, resources=None, **other_settings)
live.contributor()
live.contributor.accept_invite()
live.contributor.invite(redditor, permissions=None)
live.contributor.leave()
live.contributor.remove(redditor)
live.contributor.remove_invite(redditor)
live.contributor.thread()
live.contributor.update(redditor, permissions=None)
live.contributor.update_invite(redditor, permissions=None)
