#!/usr/bin/python3
"""API views for CRUD operation on State model"""
from api.v1.views import app_views
from flask import abort, jsonify
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
def get_all_states():
    """ get all objects from states table/class"""
    states = storage.all(State)
    states_lst = []

    for state in states.values():
        states_lst.append(state.to_dict())

    # or just below line
    # states_lst = [obj.to_dict() for obj in storage.all(State).values()]

    return jsonify(all_states)


@app_views.route('/states/<string:state_id>', methods=['GET'])
def get_one_state_by_id(state_id):
    """ get ONE object from states table/class
    by id, otherwise abort and raise 404 error"""
    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'])
def del_one_state_by_id(state_id):
    """ delete one objects from states table/class
    by id, otherwise abort and raise 404 error"""
    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    # id exist in states table or an object of states class
    storage.delete(state)
    # update storage to apply deleting
    storage.save()
    # return empty jsonified dict with 200 status code
    return jsonify({}), 200
