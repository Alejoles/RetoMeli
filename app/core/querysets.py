from core.models import ItemModel
from mongoengine.errors import NotUniqueError


class ItemRepository:
    """
        Is in charge of the database operations with the item model
    """

    @staticmethod
    def find_one_active(**params) -> ItemModel:
        return ItemModel.objects(**params).first()

    @staticmethod
    def insert_one_item(data):
        try:
            if ItemModel.objects(**data).count() > 0:
                raise NotUniqueError
            tag = ItemModel(**data)
            return tag.save()
        except NotUniqueError as e:
            return str(e)
