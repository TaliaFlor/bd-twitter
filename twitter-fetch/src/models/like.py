from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Like:
    """Represents a like given to a tweet"""
    tweet_id: int
    user_id: int

    def __iter__(self):
        return iter([self.tweet_id, self.user_id])
