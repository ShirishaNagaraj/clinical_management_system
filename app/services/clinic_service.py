from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.clinic_model import Clinic
from app.exceptions.domain_exception import ClinicNotFoundException


async def create_clinic(data, db: AsyncSession):
    clinic = Clinic(
        clinic_name=data.clinic_name,
        clinic_address=data.clinic_address,
        is_active=True
    )
    db.add(clinic)
    await db.commit()
    await db.refresh(clinic)
    return clinic


async def get_clinic(clinic_id: int, db: AsyncSession):
    clinic = await db.get(Clinic, clinic_id)
    if not clinic:
        raise ClinicNotFoundException()
    return clinic
