from sqlalchemy.ext.asyncio import AsyncSession

from app.services.patient_service import PatientService
from app.schemas.patient_schema import PatientCreate
from app.core.api_response import success_response


class PatientController:

    def __init__(self):
        self.service = PatientService()

    async def register_patient(
        self,
        data: PatientCreate,
        db: AsyncSession
    ):
        patient = await self.service.register_patient(db, data)

        return success_response(
            data={
                "patient_id": patient.patient_id,
                "clinic_id": patient.clinic_id,
                "patient_name": patient.patient_name,
                "phone_number": patient.phone_number,
                "patient_status": patient.patient_status
            },
            message="Patient registered successfully"
        )

    async def list_patients(self, db: AsyncSession):
        patient_list = await self.service.list_patients(db)

        return success_response(
            data=[
                {
                    "patient_id": patient.patient_id,
                    "clinic_id": patient.clinic_id,
                    "patient_name": patient.patient_name,
                    "phone_number": patient.phone_number,
                    "patient_status": patient.patient_status
                }
                for patient in patient_list
            ],
            message="Patients list"
        )

    async def update_patient_status(
        self,
        patient_id: int,
        status: str,
        db: AsyncSession,
        current_user: dict
    ):
        patient = await self.service.update_patient_status(
            db=db,
            patient_id=patient_id,
            new_status=status,
            user_id=current_user["user_id"]
        )

        return success_response(
            data={
                "patient_id": patient.patient_id,
                "patient_status": patient.patient_status
            },
            message="Patient status updated successfully"
        )
