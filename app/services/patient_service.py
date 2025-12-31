from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.patient_model import Patient
from app.schemas.patient_schema import PatientCreate
from app.exceptions.domain_exception import PatientNotFoundException


class PatientService:

    async def register_patient(
        self,
        db: AsyncSession,
        data: PatientCreate,
        clinic_id: int
    ):
        patient = Patient(
            clinic_id=clinic_id,
            patient_name=data.patient_name,
            phone_number=data.phone_number,
            patient_status="NEW"
        )

        db.add(patient)
        await db.commit()
        await db.refresh(patient)
        return patient

    async def list_patients(
        self,
        db: AsyncSession,
        clinic_id: int
    ):
        result = await db.execute(
            select(Patient).where(Patient.clinic_id == clinic_id)
        )
        return result.scalars().all()

    async def update_patient_status(
        self,
        db: AsyncSession,
        patient_id: int,
        new_status: str
    ):
        patient = await db.get(Patient, patient_id)
        if not patient:
            raise PatientNotFoundException()

        patient.patient_status = new_status
        await db.commit()
        await db.refresh(patient)
        return patient
