from core.querysets import ItemRepository
import logging as log


def create_item(data: dict):
    try:
        ItemRepository.insert_one_item(data)
        return {
                "message": "YES",
                "http_code": 200
            }
    except Exception as e:
        log.error(f"An error has been found inside process create_item, Error: {e}")
        return {
                "message": "Internal Server Error",
                "http_code": 500
            }
