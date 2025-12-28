from typing import Any

def success_response(data: Any = None, message: str = "Success"):
    return {
        "status": True,
        "data": data,
        "message": message
    }


def error_response(message: str, data: Any = None):
    return {
        "status": False,
        "data": data,
        "message": message
    }
