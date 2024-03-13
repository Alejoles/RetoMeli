from flask import Blueprint, Response
import json

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
    return None
