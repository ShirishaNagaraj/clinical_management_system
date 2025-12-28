from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.clinic_schema import ClinicCreate
from app.services.clinic_service import ClinicService
from app.core.api_response import success_response


class ClinicController:

    def __init__(self):
        self.service = ClinicService()

    async def create_clinic(
        self,
        data: ClinicCreate,
        db: AsyncSession,
        current_user: dict
    ):
        clinic = await self.service.create_clinic(
            db=db,
            data=data,
            user_id=current_user["user_id"]
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
