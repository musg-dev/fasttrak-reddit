import sentry_sdk
from core import reddit as bot
from core import config
from core import db

sentry_sdk.init(
    "https://606009b6ca8248659f66cff16254dc6b@o336575.ingest.sentry.io/5686160",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

def reddit_bot():
    print("The FastTRAK Reddit Interface is initializing, stand by.")
    r_api = praw.Reddit(client_id = config.CLIENT_ID, client_secret = config.CLIENT_SECRET, username = config.USERNAME, password = config.PASSWORD, user_agent = user_agent)
    print("Online with the Reddit API")
    bot.sub_scan(r_api)