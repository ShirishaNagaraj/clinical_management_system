from sqlalchemy import Column, Integer, String, ForeignKey
from db.base import Base

class Patient(Base):
    __tablename__ = "patient"

    patient_id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinic.clinic_id"), nullable=False)
    patient_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    patient_status = Column(String(20), default="NEW")  # NEW / ACTIVE / DISCHARGED
