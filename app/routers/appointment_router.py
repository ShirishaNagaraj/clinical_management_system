from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.appointment_controller import AppointmentController
from app.db.session import get_db
from app.schemas.appointment_schema import AppointmentCreate

router = APIRouter(tags=["Appointment"],
    responses={200: {"content": None}, 422: {"content": None}}
)

controller = AppointmentController()


# 🔓 NO JWT – Book appointment
@router.post("/patientappointment")
async def book_appointment(
    data: AppointmentCreate,
    db: AsyncSession = Depends(get_db)
):
    return await controller.book_appointment(
        data=data,
        db=db
    )


# 🔓 NO JWT – View all appointments
@router.get("/getpatientappointment")
async def list_appointments(
    db: AsyncSession = Depends(get_db)
):
    return await controller.list_appointments(db)


# 🔓 NO JWT – Doctor's appointments
@router.get("/doctors/{doctor_id}/appointments")
async def doctor_appointments(
    doctor_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await controller.doctor_appointments(
        doctor_id=doctor_id,
        db=db
    )
