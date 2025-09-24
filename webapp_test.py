from Webapp import app
import pytest

@pytest.fixture

def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Test Input Fields with Titles" in response.data
    assert b"Enter your full name here" in response.data
    assert b"Enter your email address here" in response.data