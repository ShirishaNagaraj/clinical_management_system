from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db.base import Base,AuditMixin

class PatientDocument(AuditMixin,Base):
    __tablename__ = "patient_document"

    document_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"), nullable=False)
    document_type = Column(String(20), nullable=False)   # ID_PROOF / REPORT
    file_name = Column(String(255), nullable=False)
    file_path = Column(Text, nullable=False)             # URL (Cloudinary) or local path
