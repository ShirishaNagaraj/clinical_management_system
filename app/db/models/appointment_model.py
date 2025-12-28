from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db.base import Base

class Appointment(Base):
    __tablename__ = "appointment"

    appointment_id = Column(Integer, primary_key=True, index=True)

    clinic_id = Column(Integer, ForeignKey("clinic.clinic_id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctor.doctor_id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"), nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    appointment_status = Column(String(20), default="BOOKED")  # BOOKED / COMPLETED / CANCELLED
