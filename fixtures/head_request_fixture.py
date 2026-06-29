import time
from typing import List, Optional
import requests
from .auth_fixture import AuthFixture

class HeadRequestFixture:
    """
    Python SLIM Decision Table fixture for HTTP HEAD requests.
    Validates headers and status codes without downloading the response body.
    """

    def __init__(self) -> None:
        self._url: str = ""
        self._key: str = ""  # The header name to lookup (e.g. Content-Type)
        self._expected_codes: List[int] = []

        self._executed: bool = False
        self._actual_status_code: int = 0
        self._response_headers: dict = {}
        self._response_time_ms: int = 0

    # Setters mapped to columns
    def set_url(self, url: str) -> None:
        self._url = url

    def set_key(self, key: str) -> None:
        self._key = key

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
            token = AuthFixture.get_stored_token()
            if token:
                headers["Authorization"] = f"Bearer {token}"

            start = time.perf_counter()
            response = requests.head(self._url, headers=headers, timeout=15)
            self._response_time_ms = int((time.perf_counter() - start) * 1000)

            self._actual_status_code = response.status_code
            self._response_headers = dict(response.headers)

            print(f"[HEAD] {self._url} -> {self._actual_status_code} ({self._response_time_ms}ms)")
            self._executed = True
            return True

        except Exception as e:
            print(f"[HEAD] Exception [{self._url}]: {str(e)}")
            return False

    # Getters/Assertions mapped to column?
    def executed(self) -> bool:
        return self._executed

    def actual_status_code(self) -> int:
        return self._actual_status_code

    def response_time(self) -> int:
        return self._response_time_ms

    def status_codes(self) -> str:
        if not self._expected_codes:
            return str(self._actual_status_code)

        if self._actual_status_code in self._expected_codes:
            return str(self._actual_status_code)

        return f"{self._actual_status_code} (expected: {self._expected_codes})"

    def header_value(self) -> str:
        """Returns the value of the header specified in 'key' (e.g. Content-Type)."""
        if not self._key:
            return "no header key set"
        return self._response_headers.get(self._key, "header not found")
