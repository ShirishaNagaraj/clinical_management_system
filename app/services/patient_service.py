from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.patient_model import Patient
from app.db.models.clinic_model import Clinic
from app.db.models.appointment_model import Appointment
from app.db.models.patient_document_model import PatientDocument
from app.exceptions.domain_exception import (
    PatientNotFoundException,
    ClinicNotFoundException
)


async def create_patient(data, db: AsyncSession):
    clinic = await db.get(Clinic, data.clinic_id)
    if not clinic:
        raise ClinicNotFoundException()

    patient = Patient(
        clinic_id=data.clinic_id,
        patient_name=data.patient_name,
        phone_number=data.phone_number,
        patient_status="NEW"
    )
    db.add(patient)
    await db.commit()
    await db.refresh(patient)
    return patient


async def list_patients(db: AsyncSession):
    result = await db.execute(
        Patient.__table__.select()
    )
    return result.fetchall()


async def update_patient_status(patient_id: int, status: str, db: AsyncSession):
    patient = await db.get(Patient, patient_id)
    if not patient:
        raise PatientNotFoundException()

    patient.patient_status = status
    await db.commit()
    return patient


# 🔥 TRANSACTION API
async def patient_visit(patient_id: int, data, db: AsyncSession):
    async with db.begin():
        patient = await db.get(Patient, patient_id)
        if not patient:
            raise PatientNotFoundException()

        patient.patient_status = "ACTIVE"

        appointment = Appointment(
            clinic_id=data.clinic_id,
            doctor_id=data.doctor_id,
            patient_id=patient_id,
            appointment_time=data.appointment_time,
            appointment_status="BOOKED"
        )
        db.add(appointment)

        document = PatientDocument(
            patient_id=patient_id,
            document_type=data.document_type,
            file_name=data.file_name,
            file_path=data.file_path
        )
        db.add(document)

    return {"patient_id": patient_id}
