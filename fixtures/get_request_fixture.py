import time
from typing import List, Optional
import requests
from .auth_fixture import AuthFixture

class GetRequestFixture:
    """
    Python SLIM Decision Table fixture for HTTP GET requests.
    Supports token injection, status code lists, response times, and key lookups.
    """

    def __init__(self) -> None:
        self._url: str = ""
        self._key: str = ""
        self._contains_text: str = ""
        self._expected_codes: List[int] = []

        self._executed: bool = False
        self._actual_status_code: int = 0
        self._response_body: str = ""
        self._response_time_ms: int = 0
        self._response_body_json: dict = {}

    # Setters mapped to columns
    def set_url(self, url: str) -> None:
        self._url = url

    def set_key(self, key: str) -> None:
        self._key = key

    def set_contains_text(self, text: str) -> None:
        self._contains_text = text

    def set_status_codes(self, codes: str) -> None:
        self._expected_codes = []
        for code in codes.split(","):
            try:
                self._expected_codes.append(int(code.strip()))
            except ValueError:
                print(f"Invalid status code configuration: {code}")

    # Action mapped to execute?
    def execute(self) -> bool:
        try:
            headers = {}
            # Auto-inject bearer token if generated
            token = AuthFixture.get_stored_token()
            if token:
                headers["Authorization"] = f"Bearer {token}"

            start = time.perf_counter()
            response = requests.get(self._url, headers=headers, timeout=15)
            self._response_time_ms = int((time.perf_counter() - start) * 1000)
            
            self._actual_status_code = response.status_code
            self._response_body = response.text
            
            try:
                self._response_body_json = response.json()
            except Exception:
                self._response_body_json = {}

            print(f"[GET] {self._url} → {self._actual_status_code} ({self._response_time_ms}ms)")
            self._executed = True
            return True

        except Exception as e:
            print(f"[GET] Exception [{self._url}]: {str(e)}")
            return False

    # Getters/Assertions mapped to column?
    def executed(self) -> bool:
        return self._executed

    def actual_status_code(self) -> int:
        return self._actual_status_code

    def response_body(self) -> str:
        return self._response_body

    def response_time(self) -> int:
        return self._response_time_ms

    def status_codes(self) -> str:
        if not self._expected_codes:
            return str(self._actual_status_code)
        
        if self._actual_status_code in self._expected_codes:
            return str(self._actual_status_code)
        
        return f"{self._actual_status_code} (expected: {self._expected_codes})"

    def json_value(self) -> str:
        """Returns the value of 'key' (or a simple $.path) from the JSON response."""
        if not self._key:
            return "no key set"
        try:
            # Support basic nested path lookup natively (e.g. $.status or $.data.id)
            if self._key.startswith("$."):
                path_parts = self._key[2:].split(".")
                val = self._response_body_json
                for part in path_parts:
                    val = val[part]
                return str(val)
            else:
                # Standard flat key lookup fallback
                return str(self._response_body_json.get(self._key, "key not found"))
        except Exception:
            return "key not found"

    def contains_text(self) -> bool:
        if not self._contains_text:
            return True
        return self._contains_text in self._response_body
