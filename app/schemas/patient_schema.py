from pydantic import BaseModel
from app.schemas.base_schema import AuditSchema

class PatientCreate(BaseModel):
    clinic_id: int
    patient_name: str
    phone_number: str


class PatientResponse(AuditSchema):
    patient_id: int
    clinic_id: int
    patient_name: str
    phone_number: str
    patient_status: str
