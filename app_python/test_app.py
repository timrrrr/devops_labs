import pytest
# from .app import create_app

from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_200(client):
    """asserts if response status code is not 200 ok"""
    response = client.get("/")
    assert response.status_code == 200