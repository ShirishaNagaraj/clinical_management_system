import os
import uuid
import cloudinary
import cloudinary.uploader
from fastapi import UploadFile
from app.core.config import settings

UPLOAD_DIR = "uploads/patients"

# Cloudinary config
cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
)

# ---------- BASE ----------
class FileStorage:
    async def upload(self, file: UploadFile, patient_id: int) -> str:
        raise NotImplementedError


# ---------- LOCAL STORAGE (PDF, DOC) ----------
class LocalFileStorage(FileStorage):
    async def upload(self, file: UploadFile, patient_id: int) -> str:
        folder = f"{UPLOAD_DIR}/{patient_id}"
        os.makedirs(folder, exist_ok=True)

        filename = f"{uuid.uuid4()}_{file.filename}"
        path = f"{folder}/{filename}"

        with open(path, "wb") as f:
            f.write(await file.read())

        return path


# ---------- CLOUDINARY STORAGE (IMAGES) ----------
class CloudinaryStorage(FileStorage):
    async def upload(self, file: UploadFile, patient_id: int) -> str:
        result = cloudinary.uploader.upload(
            await file.read(),
            folder=f"patients/{patient_id}"
        )
        return result["secure_url"]


# ---------- FACTORY ----------
def get_storage(file: UploadFile) -> FileStorage:
    if file.content_type.startswith("image/"):
        return CloudinaryStorage()
    return LocalFileStorage()
