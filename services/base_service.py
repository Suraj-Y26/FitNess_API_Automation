import requests
from typing import Dict, Any, Optional
from utils.config import Config
from utils.logger import logger, log_request, log_response

class BaseService:
    """Base class for all API services. Handles standard HTTP methods, logging, and error tracking."""

    def __init__(self) -> None:
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT
        self.headers = Config.get_headers()

    def _send_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        """
        Sends an HTTP request, logs request/response details, and manages errors.
        
        Args:
            method: HTTP verb (GET, POST, PUT, DELETE).
            endpoint: URL path relative to base URL.
            params: Query parameters.
            json_data: Request payload body.
            
        Returns:
            requests.Response object.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        log_request(method, url, headers=self.headers, payload=json_data)
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                params=params,
                json=json_data,
                timeout=self.timeout
            )
            log_response(response.status_code, response.text, response.headers)
            return response
            
        except requests.exceptions.Timeout as e:
            logger.error(f"HTTP Request Timeout on {method} {url}: {str(e)}")
            raise
        except requests.exceptions.ConnectionError as e:
            logger.error(f"HTTP Connection Error on {method} {url}: {str(e)}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"HTTP Request failed on {method} {url}: {str(e)}")
            raise
