from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base,AuditMixin

class Clinic(AuditMixin,Base):
    __tablename__ = "clinic"

    clinic_id = Column(Integer, primary_key=True, index=True)
    clinic_name = Column(String(100), nullable=False)
    clinic_address = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
