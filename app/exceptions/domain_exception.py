from .base_exception import AppException

# ---------- CLINIC ----------
class ClinicNotFoundException(AppException):
    def __init__(self):
        super().__init__("Clinic not found", 404)

class ClinicInactiveException(AppException):
    def __init__(self):
        super().__init__("Clinic is inactive", 400)


# ---------- DOCTOR ----------
class DoctorNotFoundException(AppException):
    def __init__(self):
        super().__init__("Doctor not found", 404)

class DoctorInactiveException(AppException):
    def __init__(self):
        super().__init__("Doctor is inactive", 400)


# ---------- PATIENT ----------
class PatientNotFoundException(AppException):
    def __init__(self):
        super().__init__("Patient not found", 404)

class InvalidPatientStatusException(AppException):
    def __init__(self):
        super().__init__("Invalid patient status", 400)


# ---------- APPOINTMENT ----------
class AppointmentNotFoundException(AppException):
    def __init__(self):
        super().__init__("Appointment not found", 404)

class AppointmentSlotUnavailableException(AppException):
    def __init__(self):
        super().__init__("Appointment slot not available", 400)


# ---------- PATIENT DOCUMENT ----------
class DocumentUploadException(AppException):
    def __init__(self):
        super().__init__("Document upload failed", 500)

class InvalidDocumentTypeException(AppException):
    def __init__(self):
        super().__init__("Invalid document type", 400)
