import requests

class AuthFixture:
    """
    Python SLIM Decision Table fixture for bearer-token authentication.
    Generates a token via POST login and stores it statically so all other
    fixtures (Get/Post/Put/Patch/Delete) pick it up automatically.
    """
    _auth_token = ""  # Static/Class variable to share token across requests

    def __init__(self) -> None:
        self._token_url: str = ""
        self._body_json: str = "{}"
        self._token_field: str = "token"

    @classmethod
    def get_stored_token(cls) -> str:
        """Returns the currently stored bearer token."""
        return cls._auth_token

    @classmethod
    def set_stored_token(cls, token: str) -> None:
        """Sets the stored bearer token statically."""
        cls._auth_token = token

    @classmethod
    def clear_token(cls) -> None:
        """Clears the stored token."""
        cls._auth_token = ""

    # Setters mapped to columns
    def set_token_url(self, token_url: str) -> None:
        self._token_url = token_url

    def set_body_json(self, body_json: str) -> None:
        self._body_json = body_json

    def set_token_field(self, token_field: str) -> None:
        self._token_field = token_field

    # Action mapped to execute
    def generate_token(self) -> bool:
        """Sends a POST request to generate the token and stores it statically."""
        try:
            headers = {"Content-Type": "application/json"}
            # Send raw body
            response = requests.post(self._token_url, data=self._body_json, headers=headers, timeout=15)
            
            if response.status_code != 200:
                print(f"[Auth] FAILED code={response.status_code} body={response.text}")
                return False

            try:
                json_data = response.json()
            except Exception:
                print(f"[Auth] Invalid JSON response body: {response.text}")
                return False

            # Extract the token field (supports nested dictionary optString fallback)
            token = json_data.get(self._token_field, "")
            if not token:
                print(f"[Auth] Token field '{self._token_field}' not found in response: {response.text}")
                return False

            AuthFixture._auth_token = str(token)
            print("[Auth] Token acquired successfully.")
            return True

        except Exception as e:
            print(f"[Auth] Exception: {str(e)}")
            return False
