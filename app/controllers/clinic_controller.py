from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.db.session import get_db
from app.services.clinic_service import ClinicService
from app.schemas.clinic_schema import ClinicCreate
from app.dependencies.authorization_dependency import get_current_user
from app.core.api_response import success_response, error_response
from app.exceptions.base_exception import AppException


class ClinicController:

    def __init__(self):
        self.service = ClinicService()

    async def create_clinic(
        self,
        request: ClinicCreate,
        db: AsyncSession = Depends(get_db),
        current_user: dict = Depends(get_current_user)
    ):
        try:
            clinic = await self.service.create_clinic(
                db=db,
                data=request,
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

        except AppException as e:
            return error_response(message=e.message)
