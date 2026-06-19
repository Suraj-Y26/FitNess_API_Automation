import pytest
from services.user_service import UserService

@pytest.fixture
def user_service() -> UserService:
    return UserService()


def test_get_user_success(user_service: UserService) -> None:
    """Verifies that retrieving a user works and returns 200 status code."""
    response = user_service.get_user(2)
    assert response.status_code == 200
    
    data = response.json()
    assert "email" in data
    assert data["email"] == "Shanna@melissa.tv"


def test_create_user_success(user_service: UserService) -> None:
    """Verifies that creating a user works and returns 201 status code."""
    response = user_service.create_user("John", "QA")
    assert response.status_code == 201
    
    data = response.json()
    assert "id" in data


def test_update_user_success(user_service: UserService) -> None:
    """Verifies that updating a user works and returns 200 status code."""
    response = user_service.update_user(2, "John Updated", "Lead QA")
    assert response.status_code == 200


def test_delete_user_success(user_service: UserService) -> None:
    """Verifies that deleting a user works and returns 200 status code on JSONPlaceholder."""
    response = user_service.delete_user(2)
    assert response.status_code == 200
