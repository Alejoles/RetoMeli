from mongoengine import (
    Document,
    StringField,
    FloatField,
    DateTimeField,
)


class ItemModel(Document):
    meta = {"collection": "items"}
    site = StringField()
    file_id = StringField()
    price = FloatField()
    start_time = DateTimeField()
    name = StringField()
    description = StringField()
    nickname = StringField()