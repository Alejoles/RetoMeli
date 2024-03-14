from core.querysets import ItemRepository
from core.webservice import BaseResponse, HttpCode


def create_item(data: dict):
    try:
        ItemRepository.insert_one_item(data)
        return {
                "message": "YES",
                "http_code": HttpCode.OK
            }
    except Exception as e:
        print(f"An error has been found inside process create_item, Error: {e}")
        return BaseResponse(
                message="Internal Server Error",
                http_code=HttpCode.INTERNAL_SERVER_ERROR
            )
