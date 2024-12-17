def test_register(client):
    response = client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'securepassword',
        'role': 'user'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'User registered successfully'

def test_login(client):
    # First, register the user
    client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'securepassword',
        'role': 'user'
    })

    # Then, login
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'securepassword'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_protected_route(client):
    # Register and login to get token
    client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'securepassword',
        'role': 'user'
    })
    login_response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'securepassword'
    })
    token = login_response.json['access_token']

    # Test protected route
    response = client.get('/auth/me', headers={
        'Authorization': f'Bearer {token}'
    })
    assert response.status_code == 200
    assert response.json['username'] == 'testuser'
