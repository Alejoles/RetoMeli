from enum import Enum, unique
import core.constants as constants


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


class WebService:

    def __init__(self) -> None:
        self.base_url = constants.BASE_API_URL
        self.items_attributes = constants
        self.multiget_size = 10

    def get_data_from_items(self):
        items_url = self.base_url + "items"
        query_params = ""
