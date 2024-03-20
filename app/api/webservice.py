from enum import Enum, unique
from core import constants
import requests


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
    """
        Webservice is a singleton class that manages
        all requests to be made to the meli API.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        self.base_url = constants.BASE_API_URL
        self.multiget_size = int(constants.MULTIGET_SIZE)

    def get_data_from_items(self, ids: list):
        """
            Method used to fetch data from the item endpoint.
        """
        items_url = self.base_url + "items"
        query_params = {
            'ids': ','.join(ids),
            'attributes': 'price,start_time,category_id,currency_id,seller_id'
            }
        response = requests.get(items_url, params=query_params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error while getting items. Status code: : {response.status_code}")
            return None

    def get_data_from_categories(self, category_id: str):
        categories_url = self.base_url + f"categories/{category_id}"
        response = requests.get(categories_url)
        if response.status_code == 200:
            data = response.json()
            return data['name']
        else:
            print(f"Error while getting categories. Status code: {response.status_code}")
            return None

    def get_data_from_currencies(self, currency_id: str):
        currency_url = self.base_url + f"currencies/{currency_id}"
        response = requests.get(currency_url)
        if response.status_code == 200:
            data = response.json()
            return data['description']
        else:
            print(f"Error while getting currencies. Status code: {response.status_code}")
            return None

    def get_data_from_users(self, seller_id: str):
        users_url = self.base_url + f"users/{seller_id}"
        response = requests.get(users_url)
        if response.status_code == 200:
            data = response.json()
            return data['nickname']
        else:
            print(f"Error while getting user. Status code: {response.status_code}")
            return None
