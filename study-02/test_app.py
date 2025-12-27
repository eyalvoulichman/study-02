import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client, mocker):
    # Mock the get_hit_count function to avoid needing a real Redis
    mocker.patch('app.get_hit_count', return_value=1)
    
    rv = client.get('/')
    assert b'Hello World! I have been seen 1 times.' in rv.data

def test_health_route_up(client, mocker):
    # Mock redis ping to succeed
    mocker.patch('app.cache.ping', return_value=True)
    
    rv = client.get('/health')
    assert rv.status_code == 200
    assert b'UP' in rv.data

