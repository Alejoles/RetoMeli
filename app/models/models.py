from mongoengine import (
    Document,
    StringField,
    FloatField,
    DateTimeField,
    IntField
)


class Item(Document):
    site = StringField(required=True)
    id = IntField(required=True, unique=True)
    price = FloatField()
    start_time = DateTimeField()
    name = StringField()
    description = StringField()
    nickname = StringField()
