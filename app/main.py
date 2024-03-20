import mongoengine
import core.constants as constants
from flask import Flask
from api.routes import (
    process_bp,
    index_bp,
    database_bp
)


app = Flask(__name__)
app.register_blueprint(index_bp, route_prefix='')
app.register_blueprint(process_bp, route_prefix='/api/v1')
app.register_blueprint(database_bp, route_prefix='/api/v1')


if __name__ == "__main__":
    mongoengine.connect(
        host=constants.MONGO_URI
    )
    app.run(debug=True, host="0.0.0.0", port=8000)
