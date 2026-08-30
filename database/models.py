from sqlalchemy import Column, Integer, String, Text
from database.db import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    title = Column(String)
    location = Column(String)
    description = Column(Text)
    apply_url = Column(String, unique=True)
    ats_score = Column(Integer)