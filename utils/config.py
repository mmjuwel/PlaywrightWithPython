import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Config:
    
    # URLs
    BASE_URL = os.getenv("BASE_URL", "https://test.rooya.ai")
    LOGIN_URL = os.getenv("LOGIN_URL", "https://test.rooya.ai/login")
    HOME_URL = os.getenv("HOME_URL", "https://test.rooya.ai/home")
    TRIPS_URL = os.getenv("TRIPS_URL", "https://test.rooya.ai/trips")
    
    # Credentials
    EMAIL = os.getenv("EMAIL", "")
    PASSWORD = os.getenv("PASSWORD", "")
    
    # Browser Configuration
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    
    # Test Configuration
    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
    SLOWMO = int(os.getenv("SLOWMO", "200"))
