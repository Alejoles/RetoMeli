from flask import Blueprint, Response
from core.process import create_item
import json
import datetime

read_bp = Blueprint('read', __name__)
index_bp = Blueprint('index', __name__)


"""
    Index path, works for testing if the service is working,
    similar to /health endpoint.
"""


@index_bp.route("/")
def index():
    data = {'Message': "Project working, go to /api/v1/docs for documentation."}
    return Response(
        json.dumps(data),
        status=200,
        mimetype='application/json'
    )


"""
    Read path
"""


@read_bp.route("/read_file")
def read_file():
    data_1 = {
        "site": "sitetest",
        "file_id": "12341245",
        "price": 5678,
        "start_time": datetime.datetime.now,
        "name": "name test",
        "description": "description test",
        "nickname": "nicknametest",
    }
    data = create_item(data_1)
    response = Response(
        json.dumps(data),
        status=data.http_code,
        mimetype='application/json'
    )
    return response
