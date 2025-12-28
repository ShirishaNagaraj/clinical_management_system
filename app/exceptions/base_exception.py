class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class ValidationException(AppException):
    def __init__(self, message: str):
        super().__init__(message, 400)