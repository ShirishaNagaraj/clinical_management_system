from pydantic import BaseModel
from app.schemas.base_schema import AuditSchema

class PatientDocumentCreate(BaseModel):
    patient_id: int
    document_type: str
    document_path: str   # file path or cloud URL


class PatientDocumentResponse(AuditSchema):
    document_id: int
    patient_id: int
    document_type: str
    document_path: str
