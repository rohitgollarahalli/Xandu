import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"PennyLane Support API is up!" in response.data
