from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'Jobs'

    id = Column(Integer, primary_key=True)
    team_leader = Column(Integer, ForeignKey('users.id'), nullable=False)
    job_description = Column(String)
    work_size_hours = Column(Integer)
    collaborators_ids = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)
    team_leader_id = relationship("User")
