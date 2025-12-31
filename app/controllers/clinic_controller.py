from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import create_access_token
from app.schemas.clinic_schema import ClinicCreate
from app.services.clinic_service import ClinicService
from app.core.api_response import success_response
from fastapi import HTTPException

class ClinicController:

    def __init__(self):
        self.service = ClinicService()

    async def create_clinic(
        self,
        data: ClinicCreate,
        db: AsyncSession
    ):
        clinic = await self.service.create_clinic(
            db=db,
            data=data,
            user_id=None
        )

        return success_response(
            data={
                "clinic_id": clinic.clinic_id,
                "clinic_name": clinic.clinic_name,
                "clinic_address": clinic.clinic_address,
                "is_active": clinic.is_active
            },
            message="Clinic created successfully"
        )
    
    def __init__(self):
        self.service = ClinicService()

    async def clinic_login(
        self,
        clinic_id: int,
        db: AsyncSession
    ):
        clinic = await self.service.get_clinic_by_id(db, clinic_id)

        if not clinic:
            return {
                "status": False,
                "message": "Invalid clinic_id"
            }

        token = create_access_token(
            {"clinic_id": clinic.clinic_id}
        )

        return {
            "status": True,
            "access_token": token,
            "token_type": "Bearer"
        }