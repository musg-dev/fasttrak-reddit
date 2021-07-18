import datetime

from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import DateTime
import bot_parser
import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import and_
import models


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
    sub.reply("Bill has been created.")
    s.close_all()


def find_bill(sub, thr_id):
    s = Session()
    s.close_all()
    bill_type = bot_parser.parse_title(sub.title)
    bill_num = bot_parser.parse_bill_num(sub.title, bill_type)[0]

    q = s.query(models.Bills).filter(and_(models.Bills.bill_type == bill_type,
                                     models.Bills.bill_number == bill_num)).first()
    #bill_id = s.query(models.Bills.id).filter(q.exists()).first()
    if not q:
        create_bill(sub, thr_id)
        q2 = s.query(models.Bills).filter(and_(models.Bills.bill_type == bill_type,
                                     models.Bills.bill_number == bill_num)).first()
        bill_id = q2.id
        return bill_id

    if q != null:
        return q.id


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


def find_user(usr_id, usr_name):
    s = Session()
    s.close_all()

    q = s.query(models.Redditors).filter(models.Redditors.user_api == usr_id).first()
    if not q:
        track_users(0, usr_name, usr_id)
        user_id = s.query(models.Redditors).filter(models.Redditors.user_api == usr_id).first()
        return user_id.id

    if q != 0:
        return q.id


def create_thread(sub, thr_id):
    s = Session()
    bill_id = find_bill(sub, thr_id)

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
    thread_id = s.query(models.Threads).filter(q.exists()).first()
    if not thread_id:
        return 0

    if thread_id != null:
        return thread_id.id


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
        old_bill = find_bill(sub, thr_id)
        create_thread(sub, thr_id)
        update_bill(old_bill, thr_id)
    if flag == 1:
        if find_thread(thr_id) == 0:
            create_thread(sub, thr_id)
        else:
            return 0


def track_users(flag, user, user_api):
    if flag == 0:
        create_user(user_api, user)
    if flag == 1:
        return find_user(user_api)
    else:
        return 0

def update_bill(bill_id, new_thr):
    s = Session()
    q = s.query(models.Bills).filter(models.Bills.id == bill_id).first()
    q.last_seen = datetime.datetime.utcnow().isoformat()
    q.last_seen_thread = new_thr
    s.commit()
    s.close_all()

def update_thread(thr_api, mode, vt_log):
    s = Session()
    thr_id = find_thread(thr_api)
    q = s.query(models.Threads).filter(models.Threads.id == thr_id).first()
    q.locked = mode
    q.votes_logged = vt_log
    q.locked_on = datetime.datetime.utcnow().isoformat()
    s.commit()
    s.close_all()
