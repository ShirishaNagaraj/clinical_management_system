from fastapi import FastAPI
from app.db.session import lifespan
from app.middleware.request_logging import request_logging_middleware

# Routers
from app.routers.clinic_router import router as clinic_router
from app.routers.doctor_router import router as doctor_router
from app.routers.patient_router import router as patient_router
from app.routers.appointment_router import router as appointment_router
from app.routers.patient_document_router import router as document_router

app = FastAPI(lifespan=lifespan)

app.middleware("http")(request_logging_middleware)

@app.get("/")
async def root():
    return {"status": True, "message": "App running"}

# Register routers
app.include_router(clinic_router)
app.include_router(doctor_router)
app.include_router(patient_router)
app.include_router(appointment_router)
app.include_router(document_router)

