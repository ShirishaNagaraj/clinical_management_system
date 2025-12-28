from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.appointment_model import Appointment
from app.exceptions.domain_exception import AppointmentNotFoundException


async def create_appointment(data, db: AsyncSession):
    appointment = Appointment(
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


async def list_appointments(db: AsyncSession):
    result = await db.execute(
        Appointment.__table__.select()
    )
    return result.fetchall()


async def doctor_appointments(doctor_id: int, db: AsyncSession):
    result = await db.execute(
        Appointment.__table__.select().where(
            Appointment.doctor_id == doctor_id
        )
    )
    return result.fetchall()
