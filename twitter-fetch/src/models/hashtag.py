from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Hashtag:
    """Represents a hashtag used in a tweet"""
    tweet_id: int
    hashtag: str

    def __iter__(self):
        return iter([self.tweet_id, self.hashtag])
