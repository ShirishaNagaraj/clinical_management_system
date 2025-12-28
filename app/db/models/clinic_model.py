from sqlalchemy import Column, Integer, String, Boolean
from db.base import Base

class Clinic(Base):
    __tablename__ = "clinic"

    clinic_id = Column(Integer, primary_key=True, index=True)
    clinic_name = Column(String(100), nullable=False)
    clinic_address = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
