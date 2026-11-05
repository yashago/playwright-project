import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str


def new_user() -> User:
    """Return a unique user so tests never collide on an existing account."""
    suffix = uuid.uuid4().hex[:12]
    return User(username=f"qa{suffix}", password=f"Pw-{uuid.uuid4().hex[:16]}")
