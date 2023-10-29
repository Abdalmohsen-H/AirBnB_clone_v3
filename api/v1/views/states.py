#!/usr/bin/python3
"""API views for CRUD operation on State model"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
def get_all_states():
    """
    get all objects from states table/class
    """
    states = storage.all(State)
    states_lst = []

    for state in states.values():
        states_lst.append(state.to_dict())

    # or just below line
    # states_lst = [obj.to_dict() for obj in storage.all(State).values()]

    return jsonify(states_lst)


@app_views.route('/states/<string:state_id>', methods=['GET'])
def get_one_state_by_id(state_id):
    """
    get ONE object from states table/class
    by id, otherwise abort and raise 404 error
    """
    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'])
def del_one_state_by_id(state_id):
    """
    delete one objects from states table/class
    by id, otherwise abort and raise 404 error
    """
    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    # id exist in states table or an object of states class
    storage.delete(state)
    # update storage to apply deleting
    storage.save()
    # return empty jsonified dict with 200 status code
    return jsonify({}), 200

@app_views.route('/states', methods=['POST'])
def create_new_state():
    """ create new state object route"""
    # get json from request
    json = request.get_json()

    # check json and if failed abort and with msg
    if not json:
        abort(400, 'Not a JSON')

    if 'name' not in json:
        abort(400, 'Missing name')

    # create new state object
    new_state = State(**json)
    # save new_stae object to apply updates
    new_state.save()

    return jsonify(new_state.to_dict()), 201

@app_views.route('/states/<string:state_id>', methods=['PUT'])
def update_state_by_id(state_id):
    """ update state object by id route"""
    # get json from request
    json = request.get_json()

    if not json:
        abort(400, 'Not a JSON')

    # get state object by id
    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    # update state object with all key-value pairs of the dictionary.
    for key, value in json.items():
        # Ignore keys: id, created_at and updated_at
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)

    # save state object to apply updates
    state.save()

    return jsonify(state.to_dict()), 200
