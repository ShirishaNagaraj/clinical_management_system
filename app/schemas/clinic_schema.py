from pydantic import BaseModel
from app.schemas.base_schema import AuditSchema

class ClinicCreate(BaseModel):
    clinic_name: str
    clinic_address: str


class ClinicResponse(AuditSchema):
    clinic_id: int
    clinic_name: str
    clinic_address: str

class ClinicLogin(BaseModel):
    clinic_id: int


class ClinicLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"