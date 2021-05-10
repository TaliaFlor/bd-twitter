from dataclasses import dataclass, field
from datetime import date


@dataclass(frozen=True, order=True)
class User:
    """Represents a Twitter user"""
    user_id: int
    email: str = field(compare=False)
    password: str = field(compare=False)
    username: str = field(compare=False)
    display_name: str = field(compare=False)
    location: str = field(default=None, compare=False)
    description: str = field(default=None, compare=False)
    verified: int = field(default=0, compare=False)  # False
    joined_on: date = field(default=None, compare=False)

    def __iter__(self):
        return iter([
            self.user_id,
            self.email,
            self.password,
            self.username,
            self.display_name,
            self.location,
            self.description,
            self.verified,
            self.joined_on
        ])
