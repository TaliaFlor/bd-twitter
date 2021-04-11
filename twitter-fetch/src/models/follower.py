from dataclasses import dataclass


@dataclass(frozen=True)
class Follower:
    """Represents a follower of a user"""
    following_id: int
    user_id: int
