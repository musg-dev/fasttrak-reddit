import sentry_sdk
import os
import praw
import config
import db
import reddit

sentry_sdk.init(
    config.SENTRY_URL,

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


def reddit_bot():
    print("The FastTRAK Reddit Interface is initializing, stand by.")
    r_api = praw.Reddit(client_id=config.CLIENT_ID,
                        client_secret=config.CLIENT_SECRET,
                        username=config.USERNAME,
                        password=config.PASSWORD,
                        user_agent=config.USER_AGENT)
    print("Online with the Reddit API")
    reddit.sub_scan(r_api)


if os.getenv("FT_FIRSTRUN") == "1":
    db.db_kickstart()
else:
    reddit_bot()
