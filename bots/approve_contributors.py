import logging
import praw
import prawcore

SUBREDDIT = 'your_subreddit'
PHRASE = 'your_phrase'
REDDIT = praw.Reddit(
    username='your_name',
    password='your_password',
    client_id='your_id',
    client_secret='your_secret',
    user_agent='script:Contributor Approval:0.1 (by /u/kimpeek)',
)
logger = logging.getLogger('Contributors')
logging.basicConfig(
    filename='error_log.txt',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s')


def main():
    sub = REDDIT.subreddit(SUBREDDIT)
    while True:
        try:
            for message in REDDIT.inbox.unread():
                if PHRASE in message.body:
                    sub.contributor.add(message.author)
                    REDDIT.inbox.mark_read([message])
                else:
                    REDDIT.inbox.mark_unread([message])
        except prawcore.exceptions.RequestException:
            continue
        except prawcore.exceptions.ServerError:
            continue
        except Exception as error:
            logger.exception(error)
            break


if __name__ == '__main__':
    main()
