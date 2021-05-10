from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, order=True)
class Retweet:
    """Represents a retweet of a tweet"""
    tweet_id: int
    user_id: int
    retweeted_on: datetime

    def __iter__(self):
        return iter([self.tweet_id, self.user_id, self.retweeted_on])
