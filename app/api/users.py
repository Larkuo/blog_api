from flask import Blueprint, request, jsonify
from flasgger import swag_from

from app.schemas.user_schema import UserSchema
from app.swagger_definitions.user_definitions import *
from app.services.user_service import *
# from app.utils.decorators import auth_required

user_blueprint = Blueprint('users', __name__, url_prefix='/users')
user_schema = UserSchema()

@user_blueprint.route('', methods=['POST'])
@swag_from(user_create_definition)
def create_user():
    data = request.get_json()
    if not data or not all(key in data for key in ('username', 'email', 'password', 'role')):
        return jsonify({'error': 'Invalid input'}), 422

    # if get_user_by_username(data['username']) | get_user_by_email(data['email']):
    # if get_user_by_email(data['email']):
        # return jsonify({'error': 'User already exists'}), 403

    new_user = create_new_user(data)
    return user_schema.jsonify(new_user), 201

@user_blueprint.route('/<int:user_id>', methods=['GET'])
@swag_from(user_detail_definition)
# @auth_required
def get_user(user_id):
    user = get_user_by_id(user_id)
    return user_schema.jsonify(user), 200

@user_blueprint.route('/<int:user_id>', methods=['PUT'])
@swag_from(user_update_definition)
# @auth_required
def update_user(user_id):
    data = request.get_json()

    updated_user = update_user_by_id(user_id, data)

    return user_schema.jsonify(updated_user), 200

@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
@swag_from(user_delete_definition)
# @auth_required
def delete_user(user_id):
    delete_user_by_id(user_id)
    return jsonify({'message': 'User deleted successfully'}), 200
