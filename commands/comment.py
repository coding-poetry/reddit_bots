import praw

reddit = praw.Reddit('AUTHENTICATION')
COMMENT_ID = 'dja78ia'

comment = reddit.comment(COMMENT_ID)
comment.block()
comment.clear_vote()
comment.delete()
comment.downvote()
comment.edit(body)
comment.fullname
comment.gild()
comment.id()
comment.is_root
comment.mark_read()
comment.mark_unread()
comment.mod
comment.mod.approve()
comment.mod.distinguish(how='yes', sticky=False)  # yes, no, admin, special
comment.mod.ignore_reports()
comment.mod.remove(spam=False)
comment.mod.thing()
comment.mod.undistinguish()
comment.mod.unignore_reports()
comment.parent()
comment.permalink(fast=False)
comment.refresh()
comment.replies
comment.reply(body)
comment.report(reason)
comment.save(category=None)
comment.submission
comment.unsave()
comment.upvote()
