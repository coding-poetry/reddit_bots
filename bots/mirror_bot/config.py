"""
This file contains the basic configuration for running your bot.
Please insert the appropriate authentication information in the
corresponding areas below.

admin_user cannot be the logger or poster.
This account will receive notifications if the bot shutsdown

User Agent must be in this format: OS:App_Name:Version:(by /u/Username)
Example:    Linux:My_Bot:1 (by /u/spez)

logger = the user that will watch, but never post anything
poster = the user that will create crossposts but cannot see the private sub
"""

admin_user = ''

logger = {
    'username': '',
    'password': '',
    'client_id': '',
    'client_secret': '',
    'user_agent': ''
}

poster = {
    'username': '',
    'password': '',
    'client_id': '',
    'client_secret': '',
    'user_agent': ''
}


# --- Do not modify these values --- #
loiter = 60
max_restarts = 5

src = ''
dest = ''

log_file = 'activity_log.txt'
level = 20
disabled = False
mode = 'a'

db_file = 'my_bot.db'
