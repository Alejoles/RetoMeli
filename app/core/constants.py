import os
from dotenv import load_dotenv

load_dotenv()

# Database
MONGO_URI = os.getenv("MONGO_URI")

# MELI API DATA
BASE_API_URL = os.getenv("BASE_API_URL")

# Processing Data
SEPARATOR = os.getenv("SEPARATOR")
FILE_NAME = os.getenv("FILE_NAME")
ENCODING = os.getenv("ENCODING")
BATCH_SIZE = os.getenv("BATCH_SIZE")
MULTIGET_SIZE = os.getenv("MULTIGET_SIZE")
