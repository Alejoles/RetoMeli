from enum import Enum, unique


@unique
class HttpCode(Enum):
    # 2xx Success
    OK = 200
    CREATED = 201
    ACCEPTED = 202

    # 4xx Client Error
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    NOT_ACCEPTABLE = 406
    CONFLICT = 409

    # 5xx Server Error
    INTERNAL_SERVER_ERROR = 500


class BaseResponse:
    """Generic response used in use cases

    Attributes:
        _http_code (constants.enums.HttpCode):
            Validate http_code. Default HttpCode.OK
        message (str)
        errors (dict | list)
    """

    def __init__(
        self,
        http_code: int = None,
        message: str = "",
        data: any = None,
        errors: list = None,
    ):
        # Default HttpCode
        self._http_code: HttpCode = HttpCode.OK

        self.http_code = http_code
        self.message = message
        self.errors = errors if errors else {}
        self.data = data if data else {}

    @property
    def http_code(self) -> int:
        """int: Código http"""
        if self._http_code:
            return self._http_code.value
        return None

    @http_code.setter
    def http_code(self, http_code) -> None:
        if isinstance(http_code, HttpCode):
            self._http_code = http_code
        elif http_code:
            self._http_code = HttpCode(http_code)

    def json(self):
        return {
            'message': self.message,
            'errors': self.errors,
            'data': self.data,
        }
