# module common to each bot, initialises API object

import tweepy
import logging

logger = logging.getLogger()


def create_api():
    consumer_key = "jCuh84s3vFjOFH9VUi58vIIr6"
    consumer_secret = "VIbmaZCEf6GULkON2e3JvV5sm2DxgbSBKjj0hoq7Zb04VsRxZz"
    access_token = "1322222341301006337-93nQLN4GHcrh9imHEUyuD3kcbSuFir"
    access_token_secret = "fmb5NFdnob4ngZ7D6Cbr9oGFFIQwtct9gRnKHn3a4lbPo"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
