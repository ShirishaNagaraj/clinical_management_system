from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models.patient_model import PatientCreate
from app.exceptions.domain_exception import PatientNotFoundException


class PatientService:

    async def register_patient(
        self,
        db: AsyncSession,
        data: PatientCreate
    ) -> PatientCreate:

        patient = PatientCreate(
            clinic_id=data.clinic_id,
            patient_name=data.patient_name,
            phone_number=data.phone_number,
            patient_status="NEW"
        )

        db.add(patient)
        await db.commit()
        await db.refresh(patient)

        return patient

    async def list_patients(self, db: AsyncSession):
        result = await db.execute(select(PatientCreate))
        return result.scalars().all()

    async def update_patient_status(
        self,
        db: AsyncSession,
        patient_id: int,
        new_status: str,
        user_id: int
    ) -> PatientCreate:

        patient = await db.get(PatientCreate, patient_id)

        if not patient:
            raise PatientNotFoundException()

        patient.patient_status = new_status
        patient.updated_by = user_id

        await db.commit()
        await db.refresh(patient)

        return patient
