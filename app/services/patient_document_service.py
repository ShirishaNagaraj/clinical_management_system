from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import UploadFile
from typing import List

from app.db.models.patient_document_model import PatientDocument
from app.utils.file_utils import get_storage
from app.exceptions.base_exception import ValidationException
from app.exceptions.domain_exception import DocumentUploadException

class PatientDocumentService:

    async def upload_documents(
        self,
        db: AsyncSession,
        patient_id: int,
        files: List[UploadFile]
    ):
        if not files:
            raise ValidationException("No files provided")

        documents = []

        try:
            for file in files:
                storage = get_storage(file)
                file_path = await storage.upload(file, patient_id)

                doc = PatientDocument(
                    patient_id=patient_id,
                    document_type=file.content_type,
                    file_name=file.filename,
                    file_path=file_path
                )

                db.add(doc)
                documents.append(doc)

            await db.commit()
            return documents

        except Exception:
            await db.rollback()
            raise DocumentUploadException()
