from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.doctor_controller import DoctorController
from app.db.session import get_db
from app.dependencies.authorization_dependency import get_current_user
from app.schemas.doctor_schema import DoctorCreate

router = APIRouter(
    prefix="/doctors",
    tags=["Doctor"],
    dependencies=[Depends(get_current_user)]  # 🔐 JWT applied once
)

controller = DoctorController()


@router.post("/doctor")
async def add_doctor(
    data: DoctorCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await controller.add_doctor(
        data=data,
        db=db,
        current_user=current_user
    )


@router.get("/get")
async def list_doctors(
    db: AsyncSession = Depends(get_db)
):
    return await controller.list_doctors(db)
