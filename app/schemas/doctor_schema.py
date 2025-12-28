from pydantic import BaseModel
from app.schemas.base_schema import AuditSchema

class DoctorCreate(BaseModel):
    clinic_id: int
    doctor_name: str
    specialization: str


class DoctorResponse(AuditSchema):
    doctor_id: int
    clinic_id: int
    doctor_name: str
    specialization: str
