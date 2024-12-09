user_detail_definition = {
    "summary": "Retrieve a specific user",
    "description": "Fetches details of a user by their ID.",
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "required": True,
            "description": "The ID of the user to retrieve.",
            "schema": {"type": "integer"}
        }
    ],
    "responses": {
        200: {
            "description": "User details",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "username": "Jane Doe",
                        "email": "jane.doe@email.com",
                        "role": "administrator"
                    }
                }
            }
        },
        404: {
            "description": "User not found"
        }
    }
}

user_create_definition = {
    "summary": "Add a new user",
    "description": "Creates a new user.",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string"},
                        "password": {"type": "string"},
                        "role": {"type": "string"}
                    },
                    "required": ["username", "email", "password", "role"]
                },
                "example": {
                    "username": "Jane Doe",
                    "email": "jane.doe@email.com",
                    "password": "*************",
                    "role": "standard user"
                }
            }
        }
    },
    "responses": {
        201: {
            "description": "User created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 4,
                        "username": "Jane Doe",
                        "email": "jane.doe@email.com",
                        "role": "standard user"
                    }
                }
            }
        },
        422: {
            "description": "Invalid input data"
        },
        403: {
            "description": "User already exists"
        }
    }
}

user_update_definition = {
    "summary": "Update an existing user",
    "description": "Updates details of an existing user.",
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "required": True,
            "description": "The ID of the user to update.",
            "schema": {"type": "integer"}
        }
    ],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string"},
                        "password": {"type": "string"},
                        "role": {"type": "string"}
                    },
                    "required": ["username", "email", "password", "role"]
                },
                "example": {
                    "username": "Jane Doe",
                    "email": "jane.doe@email.com",
                    "password": "*************",
                    "role": "standard user"
                }
            }
        }
    },
    "responses": {
        200: {
            "description": "User updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 4,
                        "username": "Jane Doe",
                        "email": "jane.doe@email.com",
                        "role": "standard user"
                    }
                }
            }
        },
        404: {
            "description": "User not found"
        }
    }
}

user_delete_definition = {
    "summary": "Delete a user",
    "description": "Deletes a user by their ID.",
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "required": True,
            "description": "The ID of the user to delete.",
            "schema": {"type": "integer"}
        }
    ],
    "responses": {
        200: {
            "description": "User deleted successfully",
            "content": {
                "application/json": {
                    "example": {
                        "message": "User deleted successfully"
                    }
                }
            }
        },
        404: {
            "description": "User not found"
        }
    }
}
