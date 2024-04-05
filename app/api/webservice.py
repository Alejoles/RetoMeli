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

    def get_data_from_items(self, id: str, items_processed):
        """
            Method used to fetch data from the item endpoint.
        """
        items_url = self.base_url + f"items/{id}"
        response = requests.get(items_url)
        if response.status_code == 200:
            print("Getting item from url")
            data = response.json()
            if 'price' not in data:
                data['error'] = "Item do not have price"
                return data
            return data
        else:
            items_processed[0] += 1
            print(f"Error while getting items. Status code: : {response.status_code}")
            data = response.json()
            if 'error' not in data:
                data['error'] = f"An error has found status code: {response.status_code}"
            data["id"] = id
            return data

    def get_data_from_categories(self, category_id: str):
        """
            Method used to fetch data from the category endpoint.
            returns only the category name
        """
        categories_url = self.base_url + f"categories/{category_id}"
        response = requests.get(categories_url)
        if response.status_code == 200:
            data = response.json()
            if 'name' not in data:
                data['error'] = "Categorie do not have name"
                return data
            return data['name']
        else:
            print(f"Error while getting categories. Status code: {response.status_code}")
            return None

    def get_data_from_currencies(self, currency_id: str):
        """
            Method used to fetch data from the currencies endpoint.
            returns only the currency description
        """
        currency_url = self.base_url + f"currencies/{currency_id}"
        response = requests.get(currency_url)
        if response.status_code == 200:
            data = response.json()
            if 'description' not in data:
                data['error'] = "Currency do not have description"
                return data
            return data['description']
        else:
            print(f"Error while getting currencies. Status code: {response.status_code}")
            return None

    def get_data_from_users(self, seller_id: str):
        """
            Method used to fetch data from the users endpoint.
            returns only the user nickname
        """
        users_url = self.base_url + f"users/{seller_id}"
        response = requests.get(users_url)
        if response.status_code == 200:
            data = response.json()
            if 'nickname' not in data:
                data['error'] = "User do not have nickname"
                return data
            return data['nickname']
        else:
            print(f"Error while getting user. Status code: {response.status_code}")
            return None
