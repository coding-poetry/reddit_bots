import praw

reddit = praw.Reddit('AUTHENTICATION')
MESSAGE_ID = 'abc123'

message = inbox.message(MESSAGE_ID)
message.author
message.block
message.body
message.body_html
message.context
message.created
message.created_utc
message.dest
message.distinguished
message.first_message
message.first_message_name
message.fullname
message.id
message.likes
message.mark_read
message.mark_unread
message.name
message.new
message.num_comments
message.parent_id
message.parse
message.replies
message.reply
message.score
message.subject
message.subreddit
message.subreddit_name_prefixed
message.was_comment
