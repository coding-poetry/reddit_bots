from time import sleep, strftime, time
import configparser
import prawcore
import logging
import praw

start = time()
config = configparser.ConfigParser()
config.read('bot.conf', encoding='utf-8')
AUTH = config['AUTHENTICATION']
LOG = config['LOGGING']
logging.basicConfig(filename=LOG['logfile'], level=logging.DEBUG, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)
reddit = praw.Reddit(
    password=AUTH['password'],
    username=AUTH['username'],
    client_id=AUTH['client_id'],
    user_agent=AUTH['user_agent'],
    client_secret=AUTH['client_secret'])

logger.disabled = False
notification = False
max_restarts = 5
wait = 60


def run():
    # Stream comments or submissions
    pass


if __name__ == '__main__':
    logger.info('Start')
    restarts = 0
    while restarts < max_restarts:
        try:
            run()
        except prawcore.exceptions.OAuthException as e:
            logger.exception(e)
            break
        except prawcore.exceptions.RequestException as e:
            logger.exception(e)
            restarts += 1
            sleep(wait)
            continue
        except prawcore.exceptions.ResponseException as e:
            logger.exception(e)
            restarts += 1
            sleep(wait)
            continue
        except Exception as e:
            logger.exception(e)
            restarts += 1
            sleep(wait)
            continue
        else:
            logger.info('Max restarts exceeded')

    logger.info('Stop')
    if notification:
        reddit.redditor(AUTH['bot_owner']).message('BOT STOPPED', strftime("%Y-%m-%d %H:%M:%S"))
