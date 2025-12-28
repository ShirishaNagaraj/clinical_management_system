import time
from fastapi import Request
from app.core.logging import logger

async def request_logging_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = round(time.time() - start, 3)

    logger.info(
        f"{request.method} {request.url.path} "
        f"Status={response.status_code} "
        f"Time={duration}s"
    )
    return response
