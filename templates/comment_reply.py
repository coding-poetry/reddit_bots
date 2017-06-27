import praw

reddit = praw.Reddit('AUTHENTICATION')
for reply in reddit.inbox.comment_replies():
    reply.author
    reply.block()
    reply.body
    reply.body_html
    reply.clear_vote()
    reply.context
    reply.created
    reply.created_utc
    reply.delete()
    reply.dest
    reply.distinguished
    reply.downvote()
    reply.edit(body)
    reply.first_message
    reply.first_message_name
    reply.fullname
    reply.gild
    reply.id
    reply.is_root
    reply.likes
    reply.link_title
    reply.mark_read()
    reply.mark_unread()
    reply.mod
    reply.name
    reply.new
    reply.num_comments
    reply.parent()
    reply.parent_id
    reply.parse
    reply.permalink(fast=False)
    reply.refresh()
    reply.replies
    reply.reply(body)
    reply.report(reason)
    reply.save(category=None)
    reply.score
    reply.subject
    reply.submission
    reply.subreddit
    reply.subreddit_name_prefixed
    reply.unsave()
    reply.upvote()
    reply.was_comment
