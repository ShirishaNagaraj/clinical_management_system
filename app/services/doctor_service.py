from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models.doctor_model import Doctor
from app.db.models.clinic_model import Clinic
from app.exceptions.domain_exception import (
    ClinicNotFoundException,
    ClinicInactiveException
)
from app.schemas.doctor_schema import DoctorCreate


class DoctorService:

    async def add_doctor(
        self,
        db: AsyncSession,
        data: DoctorCreate,
        user_id: int
    ) -> Doctor:

        # Validate clinic
        result = await db.execute(
            select(Clinic).where(Clinic.clinic_id == data.clinic_id)
        )
        clinic = result.scalar_one_or_none()

        if not clinic:
            raise ClinicNotFoundException()

        if not clinic.is_active:
            raise ClinicInactiveException()

        doctor = Doctor(
            clinic_id=data.clinic_id,
            doctor_name=data.doctor_name,
            specialization=data.specialization,
            is_active=True,
            created_by=user_id
        )

        db.add(doctor)
        await db.commit()
        await db.refresh(doctor)

        return doctor

    async def list_doctors(self, db: AsyncSession):
        result = await db.execute(
            select(Doctor).where(Doctor.is_active == True)
        )
        return result.scalars().all()
