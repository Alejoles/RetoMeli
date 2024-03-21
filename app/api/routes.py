from flask import Blueprint, Response
from core.process import process_data_with_threads
import json
from core import constants

process_bp = Blueprint('process', __name__)
index_bp = Blueprint('index', __name__)
database_bp = Blueprint('database', __name__)


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
    Process path
"""


@process_bp.route("/process", methods=["GET"])
def process_file():
    data = process_data_with_threads(num_threads=int(constants.THREADS_NUMBER))
    response = Response(
        response=json.dumps({
            "message": data["message"]
            }),
        status=data["http_code"],
        mimetype='application/json'
    )
    return response


@database_bp.route("/find_one/<string:id>", methods=["GET"])
def get_item_db(id):
    print(id)
