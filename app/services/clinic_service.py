from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models.clinic_model import ClinicCreate
from app.exceptions.domain_exception import ClinicAlreadyExistsException


class ClinicService:

    async def create_clinic(
        self,
        db: AsyncSession,
        data: ClinicCreate,
        user_id: int
    ):
        # Check duplicate clinic
        result = await db.execute(
            select(ClinicCreate).where(ClinicCreate.clinic_name == data.clinic_name)
        )
        if result.scalar_one_or_none():
            raise ClinicAlreadyExistsException()

        clinic = ClinicCreate(
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
