from fixtures.base_fixture import BaseFixture
from services.user_service import UserService
from utils.logger import logger

class UserFixture(BaseFixture):
    """
    FitNesse script-compatible Fixture class.
    Exposes methods that map directly to FitNesse script tables.
    """

    def __init__(self) -> None:
        super().__init__()
        self._user_service = UserService()

    def get_user(self, user_id: str) -> bool:
        """
        Retrieves user details for the given user_id.
        Mapped to: |get user|user_id| or |get_user|user_id| in FitNesse.
        """
        try:
            # Coerce string input from FitNesse to integer
            id_val = int(user_id)
            self._last_response = self._user_service.get_user(id_val)
            return True
        except ValueError:
            logger.error(f"Invalid user_id input format: {user_id}. Must be an integer.")
            return False
        except Exception as e:
            logger.error(f"Failed to execute get_user in fixture: {str(e)}")
            return False

    def create_user(self, name: str, job: str) -> bool:
        """
        Creates a new user with name and job.
        Mapped to: |create user;|name|job| in FitNesse.
        """
        try:
            self._last_response = self._user_service.create_user(name, job)
            return True
        except Exception as e:
            logger.error(f"Failed to execute create_user in fixture: {str(e)}")
            return False

    def update_user(self, user_id: str, name: str, job: str) -> bool:
        """
        Updates an existing user.
        Mapped to: |update user;|user_id|name|job| in FitNesse.
        """
        try:
            id_val = int(user_id)
            self._last_response = self._user_service.update_user(id_val, name, job)
            return True
        except ValueError:
            logger.error(f"Invalid user_id input format for update: {user_id}. Must be an integer.")
            return False
        except Exception as e:
            logger.error(f"Failed to execute update_user in fixture: {str(e)}")
            return False

    def delete_user(self, user_id: str) -> bool:
        """
        Deletes user for the given user_id.
        Mapped to: |delete user|user_id| in FitNesse.
        """
        try:
            id_val = int(user_id)
            self._last_response = self._user_service.delete_user(id_val)
            return True
        except ValueError:
            logger.error(f"Invalid user_id input format for delete: {user_id}. Must be an integer.")
            return False
        except Exception as e:
            logger.error(f"Failed to execute delete_user in fixture: {str(e)}")
            return False
