#!/usr/bin/python3
"""API views for CRUD operation on Users model"""
from api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from models import storage
from models.base_model import BaseModel
from models.user import User


# to_json = BaseModel.to_json


@app_views.route('/users', methods=['GET'])
def Retrieves_list_of_all_User():
    """
    Get and serialize all users
    """
    all_users = storage.all(User)
    all_users_list = [user.to_json() for user in all_users.values()]
    return jsonify(all_users_list)


@app_views.route('/users/<string:user_id>', methods=['GET'])
def Retrieves_User_object(user_id):
    """
    Get a user by ID
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_views.route('/users/<string:user_id>', methods=['DELETE'])
def Deletes_User_object(user_id):
    """
    Deletes a User object
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'])
def Creates_User_POST():
    """
    Creates a User using POST
    You must use request.get_json from Flask
    to transform the HTTP body request to a dictionary

    If the HTTP body request is not valid JSON,
    raise a 400 error with the message Not a JSON

    If the dictionary doesn’t contain the key email,
    raise a 400 error with the message Missing email

    If the dictionary doesn’t contain the key password,
    raise a 400 error with the message Missing password

    Returns the new User with the status code 201
    """
    json_response = request.get_json()
    if not json_response:
        abort(400, 'Not a JSON')
    elif json_response:
        if 'email' not in json_response:
            abort(400, 'Missing email')
        if 'password' not in json_response:
            abort(400, 'Missing password')
        else:
            new_user = User(**json_response)
            new_user.save()

    if new_user:
        return jsonify(new_user.to_json()), 201


@app_views.route('/users/<string:user_id>', methods=['PUT'])
def Updates_User_object_PUT(user_id):
    """
    Updates a User object using PUT
    If the user_id is not linked to any User object,
    raise a 404 error

    You must use request.get_json from Flask
    to transform the HTTP body request to a dictionary

    If the HTTP body request is not valid JSON,
    raise a 400 error with the message Not a JSON

    Update the User object with all key-value pairs of the dictionary
    Ignore keys: id, email, created_at, and updated_at
    Returns the User object with the status code 200
    """
    json_response = request.get_json()
    if not json_response:
        abort(400, 'Not a JSON')

    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    ignored_keys = ['id', 'email', 'created_at', 'updated_at']
    for key, value in json_response.items():
        if key not in ignored_keys:
            setattr(user, key, value)
    user.save()

    return jsonify(user.to_json()), 200
