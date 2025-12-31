from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.doctor_schema import DoctorResponse
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
        clinic_id: int
    ):
        doctor = await self.service.add_doctor(
            db=db,
            data=data,
            clinic_id=clinic_id
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
    # ---------------- LIST DOCTORS BY CLINIC ----------------
    async def list_doctors_by_clinic(self,db: AsyncSession,clinic_id: int):
        doctors = await self.service.list_doctors(db, clinic_id)
        return success_response(
        data=doctors,
        message="Doctors fetched successfully"
    )

