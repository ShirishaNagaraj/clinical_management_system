from typing import List
from datetime import datetime
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.patient_model import Patient
from app.db.models.appointment_model import Appointment
from app.db.models.patient_document_model import PatientDocument
from app.exceptions.domain_exception import (
    PatientNotFoundException,
    DocumentUploadException
)
from app.utils.file_utils import get_storage


class PatientDocumentService:

    # ================================
    # 1️⃣ UPLOAD DOCUMENTS ONLY
    # ================================
    async def upload_documents(
        self,
        db: AsyncSession,
        patient_id: int,
        files: List[UploadFile]
    ):
        patient = await db.get(Patient, patient_id)
        if not patient:
            raise PatientNotFoundException()

        documents = []

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
            documents.append(document)

        await db.commit()

        return documents

    # ================================
    # 2️⃣ PATIENT VISIT (TRANSACTION)
    # ================================
    async def patient_visit(
        self,
        db: AsyncSession,
        patient_id: int
    ):
        patient = await db.get(Patient, patient_id)
        if not patient:
            raise PatientNotFoundException()

        patient.patient_status = "ACTIVE"

        await db.commit()

        return {
            "patient_id": patient_id,
            "status": "VISITED"
        }
    