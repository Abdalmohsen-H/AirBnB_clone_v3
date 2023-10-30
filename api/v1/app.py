#!/usr/bin/python3
"""This script creates a Flask web application for
an Airbnb clone project and registers a blueprint.
"""

from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv

# Create a Flask app instance
app = Flask(__name__)

# Register the blueprint 'app_views' with the Flask instance
app.register_blueprint(app_views)

# (CORS) setup
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_strg(error):
    """function that closes storage session
    for task 3 on the project
    """
    if error:
        app.logger.error(f"Unhandled exception on teardown:{error}")
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """
    function to handle 404 page not found and return 404 code
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """
    MAIN
    """
    # run your Flask server (variable app) with:
    # host = environment variable HBNB_API_HOST or 0.0.0.0 if not defined
    # port = environment variable HBNB_API_PORT or 5000 if not defined
    # threaded=True
    app.run(
        host=getenv("HBNB_API_HOST", default="0.0.0.0"),
        port=int(getenv("HBNB_API_PORT", default=5000)),
        threaded=True,
    )
