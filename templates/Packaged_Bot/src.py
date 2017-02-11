from time import sleep
import prawcore
import logging
import sqlite3
import config
import praw

logger = logging.getLogger(__name__)
reddit = praw.Reddit(**config.auth)

loiter = config.loiter
max_restarts = config.max_restarts
source = config.src
logging.basicConfig(filename=config.log_file,
                    filemode=config.mode,
                    level=config.level,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger.disabled = config.disabled
conn = sqlite3.connect(config.db_file)
c = conn.cursor()


def run():
    pass


def main():
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
            sleep(loiter)
            continue
        except prawcore.exceptions.ResponseException as e:
            logger.exception(e)
            restarts += 1
            sleep(loiter)
            continue
        except Exception as e:
            logger.exception(e)
            restarts += 1
            sleep(loiter)
            continue
    else:
        logger.info('Max restarts exceeded')
    logger.info('Stop')
    if config.admin_user:
        reddit.redditor(config.admin_user).message('YOUR BOT HAS STOPPED',
                                                   'Your Poster bot has malfunctioned.\n'
                                                   'Please review the activity log for errors.')

if __name__ == '__main__':
    main()
