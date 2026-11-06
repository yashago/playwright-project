import os
from dotenv import load_dotenv


DEFAULT_TIMEOUT_MS = int(os.getenv("DEFAULT_TIMEOUT_MS", "15000"))

load_dotenv()  # loads .env if it exists; real environment variables take priority

GITHUB_URL = "https://www.github.com"
EMAIL_GITHUB = os.getenv("EMAIL_GITHUB")
PASSWORD_GITHUB = os.getenv("PASSWORD_GITHUB")
GITHUB_USERNAME = "yashago"