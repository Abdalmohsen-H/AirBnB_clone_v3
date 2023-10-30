#!/usr/bin/python3
"""API views for CRUD operation on city model"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.city import City


@app_views.route('/cities', methods=['GET'])
def get_all_cities():
    """
    Get all objects from the cities table/class
    """
    cities = storage.all(City)
    cities_lst = [city.to_dict() for city in cities.values()]
    return jsonify(cities_lst)


@app_views.route('/cities/<string:city_id>', methods=['GET'])
def get_one_city_by_id(city_id):
    """
    Get ONE object from cities table/class by ID,
    otherwise abort and raise a 404 error
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<string:city_id>', methods=['DELETE'])
def del_one_city_by_id(city_id):
    """
    Delete one object from cities table/class by ID,
    otherwise abort and raise a 404 error
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities', methods=['POST'])
def create_new_city():
    """Create a new city object route"""
    json = request.get_json()

    if not json:
        abort(400, 'Not a JSON')

    if 'name' not in json:
        abort(400, 'Missing name')

    new_city = City(**json)
    new_city.save()

    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<string:city_id>', methods=['PUT'])
def update_city_by_id(city_id):
    """Update a city object by ID route"""
    json = request.get_json()

    if not json:
        abort(400, 'Not a JSON')

    city = storage.get(City, city_id)

    if city is None:
        abort(404)

    for key, value in json.items():
        if key not in ['id', 'created_at', 'updated_at', 'state_id']:
            setattr(city, key, value)

    city.save()

    return jsonify(city.to_dict()), 200
