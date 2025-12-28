from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime, Integer
from datetime import datetime

class Base(DeclarativeBase):
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
