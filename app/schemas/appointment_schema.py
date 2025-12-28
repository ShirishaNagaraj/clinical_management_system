from pydantic import BaseModel
from datetime import datetime
from app.schemas.base_schema import AuditSchema

class AppointmentCreate(BaseModel):
    clinic_id: int
    doctor_id: int
    patient_id: int
    appointment_time: datetime


class AppointmentResponse(AuditSchema):
    appointment_id: int
    clinic_id: int
    doctor_id: int
    patient_id: int
    appointment_time: datetime
    appointment_status: str
