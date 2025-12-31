from typing import List
from datetime import datetime
from fastapi import UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.services.patient_document_service import PatientDocumentService
from app.core.api_response import success_response, error_response
from app.exceptions.base_exception import AppException


class PatientDocument:

    def __init__(self):
        self.service = PatientDocumentService()

  
    # UPLOAD DOCUMENTS API
   
    async def upload_documents(
        self,
        patient_id: int,
        files: List[UploadFile] = File(...),
        db: AsyncSession = Depends(get_db)
    ):
        try:
            docs = await self.service.upload_documents(
                db=db,
                patient_id=patient_id,
                files=files
            )

            return success_response(
                data={"documents_uploaded": len(docs)},
                message="Documents uploaded successfully"
            )

        except AppException as e:
            return error_response(message=e.message)

    # ================================
    # 2️⃣ PATIENT VISIT API
    # ================================
    async def patient_visit(
        self,
        patient_id: int,
        db: AsyncSession
    ):
        try:
            result = await self.service.patient_visit(
                db=db,
                patient_id=patient_id
            )

            return success_response(
                data=result,
                message="Patient visit completed successfully"
            )

        except AppException as e:
            return error_response(message=e.message)
