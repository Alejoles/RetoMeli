from flask import Blueprint, Response
from core.process import process_data_with_threads, get_item_from_db
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
    data = {'Message': "Project working, read documentation to run project.",
            'Endpoints': "localhost:8000/process to run main process \
                          localhost:8000/find_one/{id} to find items inside database"}
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
    data = get_item_from_db(id)
    response = Response(
        response=json.dumps({
            "data": data["message"]
            }),
        status=data["http_code"],
        mimetype='application/json'
    )
    return response
