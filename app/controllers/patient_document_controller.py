from fastapi import UploadFile, File, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.services.patient_document_service import PatientDocumentService
from app.dependencies.authorization_dependency import get_current_user
from app.exceptions.base_exception import AppException
from app.core.api_response import success_response, error_response


class PatientDocumentController:

    def __init__(self):
        self.service = PatientDocumentService()

    async def upload_patient_documents(
        self,
        patient_id: int,
        files: List[UploadFile] = File(...),
        db: AsyncSession = Depends(get_db),
        current_user: dict = Depends(get_current_user)
    ):
        """
        Upload patient documents
        - Images → Cloudinary
        - Files (PDF/DOC) → Local
        """

        try:
            documents = await self.service.upload_documents(
                db=db,
                patient_id=patient_id,
                files=files
            )

            response_data = [
                {
                    "document_id": doc.document_id,
                    "patient_id": doc.patient_id,
                    "document_type": doc.document_type,
                    "file_name": doc.file_name,
                    "file_path": doc.file_path
                }
                for doc in documents
            ]

            return success_response(
                data=response_data,
                message="Documents uploaded successfully"
            )

        except AppException as e:
            return error_response(
                message=e.message
            )
