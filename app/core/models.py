from mongoengine import (
    Document,
    StringField,
    FloatField,
)


class ItemModel(Document):
    """
        Represents an item model in the database.

        This class defines the structure of an item stored in the database. It inherits from
        mongoengine's Document class and provides fields to store various attributes of an item.

        Attributes:
        - site (StringField): The site of the item.
        - file_id (StringField): The unique identifier of the item.
        - price (FloatField): The price of the item.
        - name (StringField): The name of the item.
        - description (StringField): The description of the item.
        - nickname (StringField): The nickname of the item.
    """
    meta = {"collection": "items"}

    site = StringField()
    file_id = StringField(unique=True)
    price = FloatField()
    name = StringField()
    description = StringField()
    nickname = StringField()

    def to_json(self):
        """
            Convert the ItemModel instance to a dictionary.

            Returns:
            dict: A dictionary containing the item's attributes.
        """
        return {
            'site': self.site,
            'file_id': self.file_id,
            'price': self.price,
            'name': self.name,
            'description': self.description,
            'nickname': self.nickname
        }
