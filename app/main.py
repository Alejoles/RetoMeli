from flask import Flask
from api.routes import (
    read_bp,
    index_bp
)


app = Flask(__name__)


app.register_blueprint(index_bp, route_prefix='')
app.register_blueprint(read_bp, route_prefix='/api/v1')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
