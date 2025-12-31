from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers.patient_controller import PatientController
from app.db.session import get_db
from app.schemas.patient_schema import PatientCreate
from app.dependencies.authorization_dependency import get_current_clinic

router = APIRouter(tags=["Patient"])

controller = PatientController()


@router.post("/patients")
async def register_patient(
    data: PatientCreate,
    db: AsyncSession = Depends(get_db),
    current_clinic = Depends(get_current_clinic)
):
    return await controller.register_patient(
        data=data,
        db=db,
        clinic_id=current_clinic.clinic_id
    )


@router.get("/patients")
async def list_patients(
    db: AsyncSession = Depends(get_db),
    current_clinic = Depends(get_current_clinic)
):
    return await controller.list_patients(
        db=db,
        clinic_id=current_clinic.clinic_id
    )


@router.put("/patients/{patient_id}/status")
async def update_patient_status(
    patient_id: int,
    status: str,
    db: AsyncSession = Depends(get_db)
):
    return await controller.update_patient_status(
        patient_id=patient_id,
        status=status,
        db=db
    )
