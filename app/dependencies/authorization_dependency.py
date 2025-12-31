from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import decode_access_token
from app.db.session import get_db
from app.db.models.clinic_model import Clinic

security = HTTPBearer()


async def get_current_clinic(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_access_token(credentials.credentials)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    clinic_id = payload.get("clinic_id")
    if not clinic_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    clinic = await db.get(Clinic, clinic_id)
    if not clinic:
        raise HTTPException(status_code=401, detail="Clinic not found")

    return clinic
