from fastapi import APIRouter
from app.controllers.patient_document_controller import PatientController

router = APIRouter(prefix="/patients", tags=["Patients"])
controller = PatientController()

router.post("/{id}/documents")(controller.upload_documents)
router.post("/{id}/visit")(controller.patient_visit)
