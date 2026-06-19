import requests
from services.base_service import BaseService
from utils.config import Config

class UserService(BaseService):
    """Service layer to handle REST API calls specifically for User endpoints on ReqRes."""

    def get_user(self, user_id: int) -> requests.Response:
        """
        Retrieves a single user by their ID.
        Endpoint: GET {API_PREFIX}/users/{user_id}
        """
        return self._send_request(method="GET", endpoint=f"{Config.API_PREFIX}/users/{user_id}")

    def create_user(self, name: str, job: str) -> requests.Response:
        """
        Creates a new user.
        Endpoint: POST {API_PREFIX}/users
        """
        payload = {
            "name": name,
            "job": job
        }
        return self._send_request(method="POST", endpoint=f"{Config.API_PREFIX}/users", json_data=payload)

    def update_user(self, user_id: int, name: str, job: str) -> requests.Response:
        """
        Updates an existing user's details by their ID.
        Endpoint: PUT {API_PREFIX}/users/{user_id}
        """
        payload = {
            "name": name,
            "job": job
        }
        return self._send_request(method="PUT", endpoint=f"{Config.API_PREFIX}/users/{user_id}", json_data=payload)

    def delete_user(self, user_id: int) -> requests.Response:
        """
        Deletes a user by their ID.
        Endpoint: DELETE {API_PREFIX}/users/{user_id}
        """
        return self._send_request(method="DELETE", endpoint=f"{Config.API_PREFIX}/users/{user_id}")
