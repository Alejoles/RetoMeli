from core.models import ItemModel


class ItemRepository:
    """
        Is in charge of the database operations with the item model
    """

    @staticmethod
    def find_one_active(**params) -> ItemModel:
        return ItemModel.objects(**params).first()

    @staticmethod
    def find_many_items(filters) -> list:
        finded_items = ItemModel.objects(**filters)
        return finded_items

    @staticmethod
    def insert_one_item(data):
        tag = ItemModel(**data)
        return tag.save()
