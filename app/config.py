import os
import mongoengine
from dotenv import load_dotenv

load_dotenv()


class ConfigClass(object):
    """ Flask-mongoengine config """
    MONGO_DB_URL = os.environ.get("MONGO_URI")
    mongoengine.connect(
        host=MONGO_DB_URL
    )
