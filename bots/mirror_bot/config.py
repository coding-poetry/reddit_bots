"""
This file contains the basic configuration for running your bot.
Please insert the appropriate authentication information in the
corresponding areas below.

logger = the user that will watch, but never post anything
poster = the user that will create crossposts but cannot see the private sub
"""

# Leave blank or enter a reddit username to receive error notifications
# Must be different from logger and poster accounts
admin_user = ''

logger = {
    'username': 'string',
    'password': 'string',
    'client_id': 'string',
    'client_secret': 'string',
    'user_agent': 'string'
}

poster = {
    'username': 'string',
    'password': 'string',
    'client_id': 'string',
    'client_secret': 'string',
    'user_agent': 'string'
}

src = ''
dest = ''

# --- Do not modify these values --- #
loiter = 60
max_restarts = 5

log_file = 'activity_log.txt'
level = 20
disabled = False
mode = 'a'

db_file = 'mirror_bot.db'
