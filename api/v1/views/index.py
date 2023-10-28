#!/usr/bin/python3
"""
index.py File that defines a view function
on route  "/status"
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify
# create a route /status on the object app_views
# that returns a JSON: "status": "OK"


@app_views.route('/status', strict_slashes=False)
def get_app_status():
    """ return status ok in json
    for task 3"""

    return (jsonify({"status": "OK"}))
