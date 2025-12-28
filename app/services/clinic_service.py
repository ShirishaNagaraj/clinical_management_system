from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.clinic_model import Clinic
from app.schemas.clinic_schema import ClinicCreate
from app.exceptions.domain_exception import ClinicInactiveException


class ClinicService:

    async def create_clinic(
        self,
        db: AsyncSession,
        data: ClinicCreate,
        user_id: int
    ):
        clinic = Clinic(
            clinic_name=data.clinic_name,
            clinic_address=data.clinic_address,
            is_active=data.is_active,
            created_by=user_id,
            updated_by=user_id
        )

        db.add(clinic)
        await db.commit()
        await db.refresh(clinic)

        return clinic
