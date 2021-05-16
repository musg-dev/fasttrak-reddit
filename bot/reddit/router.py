from . import tabulation as tab
from . import db_ops


def parse_verb(verb, comment, r):
    if verb == "secure":
        thread_id = comment.link_id[3:]
        submission = r.submission(id=thread_id)
        if not submission.mod.thing.locked:
            count = tab.tabulate_votes(submission, thread_id)
            tab.secure_thread(submission, count)
    if verb == "enable":
        thread_id = comment.link_id[3:]
        submission = r.submission(id=thread_id)
        if not submission.mod.thing.locked:
            db_ops.create_bill(submission, thread_id)
