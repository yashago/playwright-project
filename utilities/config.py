import os
from dotenv import load_dotenv


DEFAULT_TIMEOUT_MS = int(os.getenv("DEFAULT_TIMEOUT_MS", "15000"))

load_dotenv()  # loads .env if it exists; real environment variables take priority

GITHUB_URL = "https://www.github.com"
GITHUB_EMAIL = os.getenv("GITHUB_EMAIL")
GITHUB_PASSWORD = os.getenv("GITHUB_PASSWORD")
GITHUB_USERNAME = "yashago"