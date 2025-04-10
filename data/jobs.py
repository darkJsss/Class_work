from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'Jobs'

    id = Column(Integer, primary_key=True)
    team_leader = Column(Integer, ForeignKey('users.id'), nullable=False)
    job = Column(String)
    work_size = Column(Integer)
    collaborators = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    is_finished = Column(Boolean)
    team_leader_id = relationship("User")
