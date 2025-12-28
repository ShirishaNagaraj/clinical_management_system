from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.doctor_model import Doctor
from app.db.models.clinic_model import Clinic
from app.exceptions.domain_exception import (
    DoctorNotFoundException,
    ClinicNotFoundException
)


async def create_doctor(data, db: AsyncSession):
    clinic = await db.get(Clinic, data.clinic_id)
    if not clinic:
        raise ClinicNotFoundException()

    doctor = Doctor(
        clinic_id=data.clinic_id,
        doctor_name=data.doctor_name,
        specialization=data.specialization,
        is_active=True
    )
    db.add(doctor)
    await db.commit()
    await db.refresh(doctor)
    return doctor


async def list_doctors(db: AsyncSession):
    result = await db.execute(
        Doctor.__table__.select()
    )
    return result.fetchall()


async def get_doctor(doctor_id: int, db: AsyncSession):
    doctor = await db.get(Doctor, doctor_id)
    if not doctor:
        raise DoctorNotFoundException()
    return doctor
