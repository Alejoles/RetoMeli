from core.models import ItemModel
from mongoengine.errors import NotUniqueError


class ItemRepository:
    """
        Is in charge of the database operations with the item model
        This class provides methods to interact with the database related to the item model.
    """

    @staticmethod
    def find_one_active(**params) -> ItemModel:
        """
            Find a single active item based on the provided parameters.

            Parameters:
            - **params (dict): Keyword arguments representing the query parameters.

            Returns:
            ItemModel: An instance of ItemModel representing the found item, if any.
        """
        return ItemModel.objects(**params).first()

    @staticmethod
    def insert_one_item(data):
        """
            Insert a single item into the database.

            This method attempts to insert the provided data into the database as a new item.
            If the item already exists (based on provided data), a NotUniqueError is raised.

            Parameters:
            - data (dict): A dictionary containing the data for the new item.

            Returns:

            ItemModel if success
            str: A message indicating the success or failure of the insertion operation.
        """
        try:
            if ItemModel.objects(**data).count() > 0:
                raise NotUniqueError
            tag = ItemModel(**data)
            return tag.save()
        except NotUniqueError as e:
            return str(e)
