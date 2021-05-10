from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Follower:
    """Represents a follower of a user"""
    following_id: int
    user_id: int

    def __iter__(self):
        return iter([self.following_id, self.user_id])
