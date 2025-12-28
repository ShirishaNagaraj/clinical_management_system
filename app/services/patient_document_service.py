from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import UploadFile
from typing import List
from datetime import datetime

from app.db.models.patient_model import Patient
from app.db.models.appointment_model import Appointment
from app.db.models.patient_document_model import PatientDocument
from app.exceptions.domain_exception import (
    PatientNotFoundException,
    DocumentUploadException
)
from app.utils.file_utils import get_storage


class PatientService:

    async def patient_visit(
        self,
        db: AsyncSession,
        patient_id: int,
        doctor_id: int,
        appointment_time: datetime,
        files: List[UploadFile]
    ):
        try:
            async with db.begin():

                # 1️⃣ Fetch Patient
                patient = await db.get(Patient, patient_id)
                if not patient:
                    raise PatientNotFoundException()

                # 2️⃣ Update Patient Status
                patient.patient_status = "ACTIVE"
                db.add(patient)

                # 3️⃣ Create Appointment
                appointment = Appointment(
                    clinic_id=patient.clinic_id,
                    doctor_id=doctor_id,
                    patient_id=patient_id,
                    appointment_time=appointment_time,
                    appointment_status="BOOKED"
                )
                db.add(appointment)

                # 4️⃣ Upload Documents
                for file in files:
                    storage = get_storage(file)
                    path = await storage.upload(file, patient_id)

                    document = PatientDocument(
                        patient_id=patient_id,
                        document_type="IMAGE" if "image" in file.content_type else "FILE",
                        file_name=file.filename,
                        file_path=path
                    )
                    db.add(document)

            # 🔥 AUTO COMMIT if everything succeeds
            return {
                "patient_id": patient_id,
                "appointment_status": "BOOKED"
            }

        except Exception as e:
            await db.rollback()
            raise DocumentUploadException()
