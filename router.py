import tabulation as tab
import db_ops


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
        status = db_ops.find_thread(thread_id)
        if status == 0:
            db_ops.track_thread(0, submission, thread_id)
        else:
            db_ops.track_thread(1, submission, thread_id)



