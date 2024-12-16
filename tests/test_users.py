def test_create_user(client):
    user_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'securepassword',
        'role': 'user'
    }

    response = client.post('/users', json=user_data)

    assert response.status_code == 201
    assert response.json['username'] == user_data['username']
    assert 'password' not in response.json  # password should not be serialized

def test_invalid_user_missing_data(client):
    # Test with missing username
    response = client.post('/users', json={'email': 'test@example.com', 'password': 'short', 'role': 'admin'})
    assert response.status_code == 422
    assert 'error' in response.json

def test_invalid_user_exisitng_email(client):
    # Test with duplicate username
    user_data_1 = {
        'username': 'testuser' ,
        'email': 'test@example.com', 
        'password': 'password1', 
        'role': 'admin'
    }

    user_data_2 = {
        'username': 'testuser2' ,
        'email': 'test@example.com', 
        'password': 'password2', 
        'role': 'user'
    }

    client.post('/users', json=user_data_1)

    response = client.post('/users', json=user_data_2)
    assert response.status_code == 403
    assert response.json['error'] == 'User already exists'

def test_invalid_user_exisitng_username(client):
    # Test with duplicate username
    user_data_1 = {
        'username': 'testuser' ,
        'email': 'test1@example.com', 
        'password': 'password1', 
        'role': 'admin'
    }

    user_data_2 = {
        'username': 'testuser' ,
        'email': 'test2@example.com', 
        'password': 'password2', 
        'role': 'user'
    }

    client.post('/users', json=user_data_1)

    response = client.post('/users', json=user_data_2)
    assert response.status_code == 403
    assert response.json['error'] == 'User already exists'
