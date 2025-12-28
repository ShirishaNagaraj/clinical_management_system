from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AuditSchema(BaseModel):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    created_by: Optional[int]
    updated_by: Optional[int]

    class Config:
        from_attributes = True
