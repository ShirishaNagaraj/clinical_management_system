from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models.clinic_model import Clinic
from app.schemas.clinic_schema import ClinicCreate
from app.exceptions.domain_exception import ClinicAlreadyExistsException


class ClinicService:

    async def create_clinic(
        self,
        db: AsyncSession,
        data: ClinicCreate,
        user_id: int
    ) -> Clinic:

        # Check duplicate clinic
        result = await db.execute(
            select(Clinic).where(Clinic.clinic_name == data.clinic_name)
        )

        if result.scalar_one_or_none():
            raise ClinicAlreadyExistsException()

        clinic = Clinic(
            clinic_name=data.clinic_name,
            clinic_address=data.clinic_address,
            is_active=True,
            created_by=user_id
        )

        db.add(clinic)
        await db.commit()
        await db.refresh(clinic)

        return clinic
