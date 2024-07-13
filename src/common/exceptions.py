from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code: int = None
    detail: str = None

    def __init__(self, detail=None, headers=None):
        super().__init__(
            status_code=self.status_code,
            detail=detail or self.detail,
            headers=headers,
        )


class NotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Not found'


class BadRequestException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Bad request'
