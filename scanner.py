import router, mods, config, datetime
from sentry_sdk import capture_message


def sub_scan(r):
    subreddit = r.subreddit(config.WATCH_SUBS)
    print(datetime.datetime.utcnow().isoformat() + " Scanner::Sub_Scan // [INFO] The FastTRAK Reddit Interface is now running. I am monitoring the following subs: \n" + config.WATCH_SUBS + "\n")
    capture_message(datetime.datetime.utcnow().isoformat() + " Scanner::Sub_Scan // [INFO] The FastTRAK Reddit Interface is now running. I am monitoring the following subs: \n" + config.WATCH_SUBS + "\n")
    

    for comment in subreddit.stream.comments():
        if config.TRIGGER in comment.body:
            if str(comment.author) in mods.list_mods(r):
                verb = comment.body.replace(config.TRIGGER, "")
                verb = verb[1:]
                router.parse_verb(verb, comment, r)
