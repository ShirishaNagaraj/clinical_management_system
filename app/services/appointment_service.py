from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models.appointment_model import AppointmentCreate


class AppointmentService:

    async def book_appointment(
        self,
        db: AsyncSession,
        data: AppointmentCreate 
    ) -> AppointmentCreate:

        appointment = AppointmentCreate(
            clinic_id=data.clinic_id,
            doctor_id=data.doctor_id,
            patient_id=data.patient_id,
            appointment_time=data.appointment_time,
            appointment_status="BOOKED"
        )

        db.add(appointment)
        await db.commit()
        await db.refresh(appointment)

        return appointment

    async def list_appointments(self, db: AsyncSession):
        result = await db.execute(select(AppointmentCreate))
        return result.scalars().all()

    async def list_doctor_appointments(
        self,
        db: AsyncSession,
        doctor_id: int
    ):
        result = await db.execute(
            select(AppointmentCreate).where(AppointmentCreate.doctor_id == doctor_id)
        )
        return result.scalars().all()
