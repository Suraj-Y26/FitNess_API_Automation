from typing import Optional
import json
import requests

class BaseFixture:
    """Base fixture class for FitNesse SLIM integration. Holds global response state."""

    def __init__(self) -> None:
        self._last_response: Optional[requests.Response] = None

    def status_code(self) -> Optional[int]:
        """
        Returns the HTTP status code of the last completed request.
        Mapped to |check|status code|...| in FitNesse.
        """
        if self._last_response is not None:
            return self._last_response.status_code
        return None

    def response_body(self) -> Optional[str]:
        """
        Returns the pretty-printed response body wrapped in a FitNesse 
        preformatted block ({{{ ... }}}) for a beautiful, structured UI display.
        """
        if self._last_response is not None:
            try:
                # Try to parse and pretty-print JSON response
                json_data = self._last_response.json()
                pretty_json = json.dumps(json_data, indent=2)
                # Wrapping in {{{ }}} forces FitNesse to render it as a clean monospaced code block!
                return f"\n{{{{\n{pretty_json}\n}}}}\n"
            except Exception:
                # Fallback to raw text if it is not valid JSON
                return f"\n{{{{\n{self._last_response.text}\n}}}}\n"
        return None
