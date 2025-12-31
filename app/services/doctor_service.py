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
        clinic_id: int
    ) -> Doctor:
        try:
            # Validate clinic
            result = await db.execute(
                select(Clinic).where(Clinic.clinic_id == clinic_id)
            )
            clinic = result.scalar_one_or_none()

            if not clinic:
                raise ClinicNotFoundException()

            if not clinic.is_active:
                raise ClinicInactiveException()

            doctor = Doctor(
                clinic_id=clinic_id,
                doctor_name=data.doctor_name,
                specialization=data.specialization,
                is_active=True
            )

            db.add(doctor)
            await db.commit()
            await db.refresh(doctor)

            return doctor

        except (ClinicNotFoundException, ClinicInactiveException):
            await db.rollback()
            raise

        except Exception as e:
            await db.rollback()
            raise Exception(f"Failed to add doctor: {str(e)}")
        
    async def list_doctors(self,db: AsyncSession,clinic_id: int):
        result = await db.execute(select(Doctor).where(Doctor.clinic_id == clinic_id,Doctor.is_active == True))
        return result.scalars().all()
    

