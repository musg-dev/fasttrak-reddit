import datetime
from . import bot_parser
from bot import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import and_
from . import models


engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine)


def create_bill(sub, thr_id):
    s = Session()
    bill_type = bot_parser.parse_title(sub.title)
    bill_num = bot_parser.parse_bill_num(sub.title, bill_type)[0]

    bill_full = models.Bills(
        bill_type=bill_type,
        bill_number=bill_num,
        last_seen=datetime.datetime.utcnow().isoformat(),
        last_seen_thread=thr_id
    )

    s.add(bill_full)
    s.commit()
    sub.reply("Thread is enabled.")
    s.close_all()


def find_bill(sub):
    s = Session()
    s.close_all()
    bill_type = bot_parser.parse_title(sub.title)
    bill_num = bot_parser.parse_bill_num(sub.title, bill_type)[0]

    q = s.query(models.Bills).filter(and_(models.Bills.bill_type == bill_type,
                                     models.Bills.bill_number == bill_num))
    bill_id = s.query(models.Bills.id).filter(q.exists()).first().id

    if bill_id != 0:
        return bill_id
    else:
        return 0


def create_user(usr_id, usr_name):
    s = Session()

    usr_full = models.Redditors(
        user_api=usr_id,
        user_friendly=usr_name,
        active=1,
        last_seen=datetime.datetime.utcnow().isoformat()
    )

    s.add(usr_full)
    s.commit()
    s.close_all()


def find_user(user_api):
    s = Session()
    s.close_all()

    q = s.query(models.Redditors).filter(models.Redditors.user_api == user_api)
    user_id = s.query(models.Redditors.id).filter(q.exists()).first().id

    if user_id != 0:
        return user_id
    else:
        return 0


def create_thread(sub, thr_id):
    s = Session()
    bill_id = find_bill(sub)

    thread_full = models.Threads(
        timestamp=datetime.datetime.utcnow().isoformat(),
        thread_id=thr_id,
        bill_id=bill_id
    )

    s.add(thread_full)
    s.commit()
    s.close_all()


def find_thread(thr_id):
    s = Session()
    s.close_all()
    q = s.query(models.Threads).filter(models.Threads.thread_id == thr_id)
    thread_id = s.query(models.Threads).filter(q.exists()).first().id

    if thread_id != 0:
        return thread_id
    else:
        return 0


def create_vote(uid, bid, tid, vote):
    s = Session()

    vote_full = models.Votes(
        timestamp=datetime.datetime.utcnow().isoformat(),
        user_id=uid,
        bill_id=bid,
        thread_id=tid,
        vote=vote
    )

    s.add(vote_full)
    s.commit()
    s.close_all()


def track_thread(flag, sub, thr_id):
    if flag == 0:
        create_bill(sub, thr_id)
        create_thread(sub, thr_id)
    if flag == 1:
        if find_thread(thr_id) == 0:
            create_thread(thr_id)
        else:
            return 0


def track_users(flag, user, user_api):
    if flag == 0:
        create_user(user_api, user)
    if flag == 1:
        return find_user(user_api)
    else:
        return 0
