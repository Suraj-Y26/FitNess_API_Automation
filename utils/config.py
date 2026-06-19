import os
from typing import Dict, Any

class Config:
    """Centralized configuration class for the automation framework."""
    
    # Base URL for the JSONPlaceholder API (100% Free, No-Key public testing API)
    BASE_URL: str = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
    
    # Default HTTP request timeout in seconds
    TIMEOUT: int = int(os.getenv("API_TIMEOUT", "15"))
    
    # Environment name (e.g. 'dev', 'stage', 'prod')
    ENV: str = os.getenv("API_ENV", "prod")

    # API Prefix: JSONPlaceholder hosts endpoints directly at the root (e.g. /users)
    API_PREFIX: str = os.getenv("API_PREFIX", "").rstrip("/")

    @classmethod
    def get_headers(cls) -> Dict[str, str]:
        """Returns standard headers used for API requests. No keys required!"""
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "FitNessePythonFramework/1.0"
        }

    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        """Helper to print out full configuration settings."""
        return {
            "BASE_URL": cls.BASE_URL,
            "API_PREFIX": cls.API_PREFIX,
            "TIMEOUT": cls.TIMEOUT,
            "ENV": cls.ENV
        }
