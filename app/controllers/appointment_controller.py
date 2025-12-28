from sqlalchemy.ext.asyncio import AsyncSession

from app.services.appointment_service import AppointmentService
from app.schemas.appointment_schema import AppointmentCreate
from app.core.api_response import success_response


class AppointmentController:

    def __init__(self):
        self.service = AppointmentService()

    async def book_appointment(
        self,
        data: AppointmentCreate,
        db: AsyncSession
    ):
        appointment = await self.service.book_appointment(db, data)

        return success_response(
            data={
                "appointment_id": appointment.appointment_id,
                "clinic_id": appointment.clinic_id,
                "doctor_id": appointment.doctor_id,
                "patient_id": appointment.patient_id,
                "appointment_time": appointment.appointment_time,
                "appointment_status": appointment.appointment_status
            },
            message="Appointment booked successfully"
        )

    async def list_appointments(self, db: AsyncSession):
        appointment_list = await self.service.list_appointments(db)

        return success_response(
            data=[
                {
                    "appointment_id": appointment.appointment_id,
                    "clinic_id": appointment.clinic_id,
                    "doctor_id": appointment.doctor_id,
                    "patient_id": appointment.patient_id,
                    "appointment_time": appointment.appointment_time,
                    "appointment_status": appointment.appointment_status
                }
                for appointment in appointment_list
            ],
            message="Appointments list"
        )

    async def doctor_appointments(
        self,
        doctor_id: int,
        db: AsyncSession
    ):
        appointment_list = await self.service.list_doctor_appointments(
            db=db,
            doctor_id=doctor_id
        )

        return success_response(
            data=[
                {
                    "appointment_id": appointment.appointment_id,
                    "clinic_id": appointment.clinic_id,
                    "doctor_id": appointment.doctor_id,
                    "patient_id": appointment.patient_id,
                    "appointment_time": appointment.appointment_time,
                    "appointment_status": appointment.appointment_status
                }
                for appointment in appointment_list
            ],
            message="Doctor appointments list"
        )
