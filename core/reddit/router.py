import praw
from sentry_sdk import capture_message
from reddit import tabulate_votes
from reddit import secure_thread

def parse_verb(verb, comment):
    if verb == "secure":
        thread_id = comment.link_id[3:]
        submission = reddit.submission(id=thread_id)
        if submission.mod.thing.locked != True:
            count = tabulate_votes(submission)
            secure_thread(submission, count)