from functools import wraps
from flask import request, jsonify
import os

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from app.services.user_service import get_user_by_id

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "secure_admin_token")

def admin_required(func):
    """
    Decorator to ensure that the user is authenticated as an admin.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get the Authorization header
        token = request.headers.get("Authorization")
        if not token or token != f"Bearer {ADMIN_TOKEN}":
            return jsonify({"message": "Admin access required"}), 403
        return func(*args, **kwargs)
    return wrapper

def validate_json(schema):
    """
    Decorator to validate JSON request payloads using a given schema.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Parse and validate the JSON payload
                data = request.get_json()
                errors = schema.validate(data)
                if errors:
                    return jsonify({"message": "Invalid data", "errors": errors}), 400
            except Exception as e:
                return jsonify({"message": "Invalid JSON format", "error": str(e)}), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Basic placeholder for token or session validation
        auth = request.headers.get('Authorization')
        if not auth or auth != "Bearer valid_token":
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated_function

def jwt_required_role(required_role):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            user = get_user_by_id(user_id)

            if not user or user.role != required_role:
                return jsonify({'error': 'Unauthorized'}), 403

            return function(*args, **kwargs)
        return wrapper
    return decorator