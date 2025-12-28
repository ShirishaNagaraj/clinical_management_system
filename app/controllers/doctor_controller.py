from sqlalchemy.ext.asyncio import AsyncSession

from app.services.doctor_service import DoctorService
from app.schemas.doctor_schema import DoctorCreate
from app.core.api_response import success_response


class DoctorController:

    def __init__(self):
        self.service = DoctorService()

    async def add_doctor(
        self,
        data: DoctorCreate,
        db: AsyncSession,
        current_user: dict
    ):
        doctor = await self.service.add_doctor(
            db=db,
            data=data,
            user_id=current_user["user_id"]
        )

        return success_response(
            data={
                "doctor_id": doctor.doctor_id,
                "clinic_id": doctor.clinic_id,
                "doctor_name": doctor.doctor_name,
                "specialization": doctor.specialization,
                "is_active": doctor.is_active
            },
            message="Doctor added successfully"
        )

    async def list_doctors(self, db: AsyncSession):
        doctor_list = await self.service.list_doctors(db)

        return success_response(
            data=[
                {
                    "doctor_id": doctor.doctor_id,
                    "clinic_id": doctor.clinic_id,
                    "doctor_name": doctor.doctor_name,
                    "specialization": doctor.specialization,
                    "is_active": doctor.is_active
                }
                for doctor in doctor_list
            ],
            message="Doctors list"
        )
