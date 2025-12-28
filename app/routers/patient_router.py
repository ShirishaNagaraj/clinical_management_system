from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.patient_controller import PatientController
from app.db.session import get_db
from app.dependencies.authorization_dependency import get_current_user
from app.schemas.patient_schema import PatientCreate

router = APIRouter(
    prefix="/patients",
    tags=["Patient"]
)

controller = PatientController()


# ❌ NO JWT – Register patient
@router.post("")
async def register_patient(
    data: PatientCreate,
    db: AsyncSession = Depends(get_db)
):
    return await controller.register_patient(
        data=data,
        db=db
    )


# ✅ JWT REQUIRED – List patients
@router.get("")
async def list_patients(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await controller.list_patients(db)


# ✅ JWT REQUIRED – Update patient status
@router.put("/{patient_id}/status")
async def update_patient_status(
    patient_id: int,
    status: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await controller.update_patient_status(
        patient_id=patient_id,
        status=status,
        db=db,
        current_user=current_user
    )
