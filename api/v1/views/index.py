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


@app_views.route('/status')
def get_app_status():
    """
    return status ok in json
    for task 3
    """

    return (jsonify({"status": "OK"}))


@app_views.route('/stats')
def model_objs_count():
    """
    Task 4 Function that uses methods added on task2 to return count
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
