from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Threads(Base):
    __tablename__ = 'threads'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    thread_id = Column(String)
    bill_id = Column(Integer)
    comm_id = Column(Integer)
    locked = Column(Boolean)
    locked_on = Column(DateTime)
    votes_logged = Column(Boolean)
    
    def __repr__(self):
        return "<Post(timestamp={}, thread_id='{}', bill_id={}, locked={}, locked_on={}, votes_logged={})>"\
                .format(self.timestamp, self.thread_id, self.bill_id, self.locked, self.locked_on, self.votes_logged)


class Votes(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    user_id = Column(Integer)
    bill_id = Column(Integer)
    thread_id = Column(Integer)
    vote = Column(Integer)

    def __repr__(self):
        return "<Votes(timestamp={}, user_api='{}', bill_id={}, thread_id={}, vote={}>"\
            .format(self.timestamp, self.user_id, self.bill_id, self.thread_id, self.vote)


class Redditors(Base):
    __tablename__ = 'redditors'
    id = Column(Integer, primary_key=True)
    user_friendly = Column(String)
    user_api = Column(String)
    active = Column(Boolean)
    last_seen = Column(DateTime)

    def __repr__(self):
        return "<Votes(user_friendly='{}', user_api='{}', active={}, last_seen={}>"\
            .format(self.user_friendly, self.user_api, self.active, self.last_seen)


class Bills(Base):
    __tablename__ = 'bills'
    id = Column(Integer, primary_key=True)
    bill_type = Column(Integer)
    bill_number = Column(Integer)
    curr_comm = Column(Integer)
    last_seen = Column(DateTime)
    last_seen_thread = Column(String)

    def __repr__(self):
        return "<Votes(bill_type={}, bill_number={}, last_seen={}, last_seen_thread='{}'>"\
            .format(self.bill_type, self.bill_number, self.last_seen, self.last_seen_thread)



