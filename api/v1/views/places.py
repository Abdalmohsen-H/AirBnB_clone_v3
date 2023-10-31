#!/usr/bin/python3
"""API views for CRUD operation on State model"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.city import City


@app_views.route('/cities/<string:city_id>/places', methods=['GET'])
def Retrieves_list_of_all_Place(city_id):
    """
    Get ONE object from cities table/class by ID,
    otherwise abort and raise a 404 error
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())
