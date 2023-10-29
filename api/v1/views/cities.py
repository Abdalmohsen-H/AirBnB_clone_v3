#!/usr/bin/python3
"""API views for CRUD operation on city model"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.city import City


@app_views.route('/cities', methods=['GET'])
def get_all_cities():
    """
    get all objects from cities table/class
    """
    cities = storage.all(city)
    cities_lst = []

    for city in cities.values():
        cities_lst.append(city.to_dict())

    # or just below line
    # cities_lst = [obj.to_dict() for obj in storage.all(city).values()]

    return jsonify(cities_lst)


@app_views.route('/cities/<string:city_id>', methods=['GET'])
def get_one_city_by_id(city_id):
    """
    get ONE object from cities table/class
    by id, otherwise abort and raise 404 error
    """
    city = storage.get(city, city_id)

    if city is None:
        abort(404)

    return jsonify(city.to_dict())


@app_views.route('/cities/<string:city_id>', methods=['DELETE'])
def del_one_city_by_id(city_id):
    """
    delete one objects from cities table/class
    by id, otherwise abort and raise 404 error
    """
    city = storage.get(city, city_id)

    if city is None:
        abort(404)

    # id exist in cities table or an object of cities class
    storage.delete(city)
    # update storage to apply deleting
    storage.save()
    # return empty jsonified dict with 200 status code
    return jsonify({}), 200


@app_views.route('/cities', methods=['POST'])
def create_new_city():
    """ create new city object route"""
    # get json from request
    json = request.get_json()

    # check json and if failed abort and with msg
    if not json:
        abort(400, 'Not a JSON')

    if 'name' not in json:
        abort(400, 'Missing name')

    # create new city object
    new_city = city(**json)
    # save new_stae object to apply updates
    new_city.save()

    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<string:city_id>', methods=['PUT'])
def update_city_by_id(city_id):
    """ update city object by id route"""
    # get json from request
    json = request.get_json()

    if not json:
        abort(400, 'Not a JSON')

    # get city object by id
    city = storage.get(city, city_id)

    if city is None:
        abort(404)

    # update city object with all key-value pairs of the dictionary.
    for key, value in json.items():
        # Ignore keys: id, created_at and updated_at
        if key not in ['id', 'created_at', 'updated_at', 'state_id']:
            setattr(city, key, value)

    # save city object to apply updates
    city.save()

    return jsonify(city.to_dict()), 200
