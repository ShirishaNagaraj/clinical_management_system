from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.doctor_model import Doctor

class DoctorService:
    async def create_doctor(self, db: AsyncSession, data, user_id: int):
        doctor = Doctor(
            clinic_id=data.clinic_id,
            doctor_name=data.doctor_name,
            specialization=data.specialization,
            is_active=True,
            created_by=user_id,
            updated_by=user_id
        )
        db.add(doctor)
        await db.commit()
        await db.refresh(doctor)
        return doctor
