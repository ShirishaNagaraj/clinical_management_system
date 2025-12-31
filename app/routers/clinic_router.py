from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.clinic_model import Clinic
from app.controllers.clinic_controller import ClinicController
from app.db.session import get_db
from app.schemas.clinic_schema import ClinicCreate,ClinicLogin
from app.core.security import create_access_token
from fastapi import HTTPException
from sqlalchemy import select



router = APIRouter(tags=["clinic"],responses={200: {"content": None}, 422: {"content": None}})

controller = ClinicController()


@router.post("/clinic")
async def create_clinic(
    data: ClinicCreate,
    db: AsyncSession = Depends(get_db)
):
    return await controller.create_clinic(
        data=data,
        db=db
    )

@router.post("/login")
async def clinic_login(
    data: ClinicLogin,
    db: AsyncSession = Depends(get_db)
):
    return await controller.clinic_login(
        clinic_id=data.clinic_id,
        db=db
    )