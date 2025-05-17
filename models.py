from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    english = Column(String)
    polish = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
