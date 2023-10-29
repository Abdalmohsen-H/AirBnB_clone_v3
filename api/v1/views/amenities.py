#!/usr/bin/python3
"""API views for CRUD operation on amenity model"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.amenity import amenity


@app_views.route('/amenities', methods=['GET'])
def get_all_amenities():
    """
    get all objects from amenities table/class
    """
    amenities = storage.all(amenity)
    amenities_lst = []

    for amenity in amenities.values():
        amenities_lst.append(amenity.to_dict())

    # or just below line
    # amenities_lst = [obj.to_dict() for obj in storage.all(amenity).values()]

    return jsonify(amenities_lst)


@app_views.route('/amenities/<string:amenity_id>', methods=['GET'])
def get_one_amenity_by_id(amenity_id):
    """
    get ONE object from amenities table/class
    by id, otherwise abort and raise 404 error
    """
    amenity = storage.get(amenity, amenity_id)

    if amenity is None:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'])
def del_one_amenity_by_id(amenity_id):
    """
    delete one objects from amenities table/class
    by id, otherwise abort and raise 404 error
    """
    amenity = storage.get(amenity, amenity_id)

    if amenity is None:
        abort(404)

    # id exist in amenities table or an object of amenities class
    storage.delete(amenity)
    # update storage to apply deleting
    storage.save()
    # return empty jsonified dict with 200 status code
    return jsonify({}), 200

@app_views.route('/amenities', methods=['POST'])
def create_new_amenity():
    """ create new amenity object route"""
    # get json from request
    json = request.get_json()

    # check json and if failed abort and with msg
    if not json:
        abort(400, 'Not a JSON')

    if 'name' not in json:
        abort(400, 'Missing name')

    # create new amenity object
    new_amenity = amenity(**json)
    # save new_stae object to apply updates
    new_amenity.save()

    return jsonify(new_amenity.to_dict()), 201

@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'])
def update_amenity_by_id(amenity_id):
    """ update amenity object by id route"""
    # get json from request
    json = request.get_json()

    if not json:
        abort(400, 'Not a JSON')

    # get amenity object by id
    amenity = storage.get(amenity, amenity_id)

    if amenity is None:
        abort(404)

    # update amenity object with all key-value pairs of the dictionary.
    for key, value in json.items():
        # Ignore keys: id, created_at and updated_at
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)

    # save amenity object to apply updates
    amenity.save()

    return jsonify(amenity.to_dict()), 200
