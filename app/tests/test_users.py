import pytest
from app.services import user_service

def test_create_user(test_db):
    user = user_service.create_user(
        test_db,
        UserCreate(
            email="test@example.com",
            password="test123",
            full_name="Test User"
        )
    )
    assert user.email == "test@example.com"
    assert user.full_name == "Test User"

def test_get_user(test_db, client):
    # Create user first
    user_data = {
        "email": "test@example.com",
        "password": "test123",
        "full_name": "Test User"
    }
    response = client.post("/api/v1/auth/register", json=user_data)
    user_id = response.json()["id"]
    
    # Login to get token
    response = client.post(
        "/api/v1/auth/token",
        data={"username": "test@example.com", "password": "test123"}
    )
    token = response.json()["access_token"]
    
    # Get user details
    response = client.get(
        f"/api/v1/users/{user_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
