from pydantic import BaseModel
from app.schemas.base_schema import AuditSchema
from datetime import datetime


class PatientDocumentCreate(BaseModel):
    patient_id: int
    document_type: str
    document_path: str   # file path or cloud URL


class PatientDocumentResponse(AuditSchema):
    document_id: int
    patient_id: int
    document_type: str
    file_name: str
    file_path: str

class PatientVisitCreate(BaseModel):
    patient_id: int
    