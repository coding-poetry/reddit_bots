import praw

reddit = praw.Reddit('AUTHENTICATION')
SUBMISSION_ID = 'abc123'

submission = reddit.submission(SUBMISSION_ID)
submission.approved_by()
submission.archived()
submission.author()
submission.author_flair_css_class()
submission.author_flair_text()
submission.banned_by()
submission.brand_safe()
submission.can_gild()
submission.clear_vote()
submission.clicked()
submission.comment_limit()
submission.comment_sort()
submission.comments()
submission.comments.list()
submission.comments.replace_more()
submission.contest_mode()
submission.created()
submission.created_utc()
submission.delete()
submission.distinguished()
submission.domain()
submission.downs()
submission.downvote()
submission.duplicates()
submission.edit(body)
submission.edited()
submission.flair()
submission.flair.choices()
submission.flair.select()
submission.flair.submission()
submission.fullname
submission.gild()
submission.gilded()
submission.hidden()
submission.hide(other_submissions=None)
submission.hide_score()
submission.id()
submission.id_from_url(url)
submission.is_self()
submission.is_video()
submission.likes()
submission.link_flair_css_class()
submission.link_flair_text()
submission.locked()
submission.media()
submission.media_embed()
submission.mod()
submission.mod.approve()
submission.mod.contest_mode(state=True)
submission.mod.distinguish(how='yes', sticky=False)
submission.mod.flair(text='', css_class='')
submission.mod.ignore_reports()
submission.mod.lock()
submission.mod.nsfw()
submission.mod.remove(spam=False)
submission.mod.sfw()
submission.mod.spoiler()
submission.mod.sticky(state=True, bottom=True)
submission.mod.suggested_sort(sort='blank')
submission.mod.thing()
submission.mod.undistinguish()
submission.mod.unignore_reports()
submission.mod.unlock()
submission.mod.unspoiler()
submission.mod_reports()
submission.name()
submission.num_comments()
submission.num_reports()
submission.over_18()
submission.parse()
submission.permalink()
submission.post_hint()
submission.preview()
submission.quarantine()
submission.removal_reason()
submission.reply(body)
submission.report(reason)
submission.report_reasons()
submission.save(category=None)
submission.saved()
submission.score()
submission.secure_media()
submission.secure_media_embed()
submission.selftext()
submission.selftext_html()
submission.shortlink
submission.spoiler()
submission.stickied()
submission.subreddit()
submission.subreddit_id()
submission.subreddit_name_prefixed()
submission.subreddit_type()
submission.suggested_sort()
submission.thumbnail()
submission.thumbnail_height()
submission.thumbnail_width()
submission.title()
submission.unhide(other_submissions=None)
submission.unsave()
submission.ups()
submission.upvote()
submission.url()
submission.user_reports()
submission.view_count()
submission.visited()
