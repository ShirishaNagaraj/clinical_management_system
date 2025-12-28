from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from db.base import Base

class Doctor(Base):
    __tablename__ = "doctor"

    doctor_id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinic.clinic_id"), nullable=False)
    doctor_name = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
