from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers.doctor_controller import DoctorController
from app.db.session import get_db
from app.schemas.doctor_schema import DoctorCreate
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.dependencies.authorization_dependency import get_current_clinic

router = APIRouter(
    tags=["Doctor"],responses= {200: {"content": None}, 422: {"content": None}}
)

controller = DoctorController()

security=HTTPBearer()
@router.post("/doctor")
async def add_doctor(
    data: DoctorCreate,
    db: AsyncSession = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security),  
    current_clinic = Depends(get_current_clinic),


):
    return await controller.add_doctor(
        data=data,
        clinic_id=current_clinic.clinic_id, 
        db=db
    )

@router.get("/doctor")
async def get_doctors(
    db: AsyncSession = Depends(get_db),
    current_clinic = Depends(get_current_clinic)
):
    return await controller.list_doctors_by_clinic(
        db=db,
        clinic_id=current_clinic.clinic_id
    )