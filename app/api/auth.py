from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from jsonschema import ValidationError
from app.models.user import User
from app import db
from app.schemas.user_schema import UserSchema
from app.services.user_service import create_new_user, get_user_by_email, get_user_by_id, get_user_by_username

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_schema = UserSchema()

    # Validate data
    try:
        user_data = user_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check for existing user
    if get_user_by_email(user_data['email']):
        return jsonify({'error': 'Email already exists'}), 400

    if get_user_by_username(user_data['username']):
        return jsonify({'error': 'Username already exists'}), 400

    # Create and save user
    new_user = create_new_user(user_data)

    return jsonify({'message': 'User registered successfully'}), 201


@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = get_user_by_email(email)
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid email or password'}), 401

    # Generate JWT token
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200


@auth_blueprint.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user_schema = UserSchema()
    return jsonify(user_schema.dump(user)), 200
