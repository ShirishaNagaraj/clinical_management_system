from typing import List
from datetime import datetime

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.patient_document_controller import PatientController
from app.db.session import get_db

router = APIRouter(
    prefix="/patients",
    tags=["Patient Documents"]
)

controller = PatientController()

# ==================================================
# 1️⃣ UPLOAD PATIENT DOCUMENTS
# POST /patients/{patient_id}/documents
# ==================================================
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


# ==================================================
# 2️⃣ PATIENT VISIT (TRANSACTION API)
# POST /patients/{patient_id}/visit
# ==================================================
@router.post("/{patient_id}/visit")
async def patient_visit(
    patient_id: int,
    doctor_id: int,
    appointment_time: datetime,
    files: List[UploadFile] = File(...),
    db: AsyncSession = Depends(get_db)
):
    return await controller.patient_visit(
        patient_id=patient_id,
        doctor_id=doctor_id,
        appointment_time=appointment_time,
        files=files,
        db=db
    )

