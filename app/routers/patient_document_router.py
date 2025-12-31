from typing import List
from app.schemas.patient_document_schema import PatientVisitCreate
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.patient_document_controller import PatientDocument
from app.db.session import get_db

router = APIRouter(
    tags=["Patient Documents"],responses={200: {"content": None}, 422: {"content": None}}
)

controller = PatientDocument()


# UPLOAD PATIENT DOCUMENTS


@router.post("/{patient_id}/documents")
async def upload_patient_documents(
    patient_id: int,
    files: List[UploadFile] = File(...),
    db: AsyncSession = Depends(get_db)
):
    return await controller.upload_documents(
        patient_id=patient_id,
        files=files,
        db=db
    )


#  PATIENT VISIT (TRANSACTION API)

@router.post("/{patient_id}/visit")
async def patient_visit(
    patient_id: int,
    data: PatientVisitCreate,
    db: AsyncSession = Depends(get_db)
):
    return await controller.patient_visit(
        patient_id=patient_id,db=db)
