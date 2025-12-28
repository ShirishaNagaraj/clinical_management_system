from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.clinic_controller import ClinicController
from app.db.session import get_db
from app.dependencies.authorization_dependency import get_current_user
from app.schemas.clinic_schema import ClinicCreate

router = APIRouter(
    prefix="/clinic",
    tags=["Clinic"],
    dependencies=[Depends(get_current_user)]  # 🔐 JWT APPLIED HERE
)

controller = ClinicController()


@router.post("/clinic")
async def create_clinic(
    data: ClinicCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await controller.create_clinic(
        data=data,
        db=db,
        current_user=current_user
    )
