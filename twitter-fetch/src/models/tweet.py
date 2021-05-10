from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True, order=True)
class Tweet:
    """Represents a tweet post. Can be an original post, a reply or a quote"""
    tweet_id: int
    user_id: int = field(compare=False)
    conversation_id: int = field(compare=False)
    content: str = field(compare=False)
    posted_on: datetime = field(compare=False)

    def __iter__(self):
        return iter([
            self.tweet_id,
            self.user_id,
            self.conversation_id,
            self.content,
            self.posted_on
        ])
