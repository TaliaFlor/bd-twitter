from typing import List

from src.models.follower import Follower
from src.models.hashtag import Hashtag
from src.models.like import Like
from src.models.mention import Mention
from src.models.retweet import Retweet
from src.models.tweet import Tweet
from src.models.user import User


class Collection:
    """Contains colletions with all the data parsed"""

    def __init__(self):
        self.users: List[User] = []
        self.followers: List[Follower] = []
        self.tweets: List[Tweet] = []
        self.hashtags: List[Hashtag] = []
        self.mentions: List[Mention] = []
        self.retweets: List[Retweet] = []
        self.likes: List[Like] = []

    # --- INSERT

    def insert_user(self, user: User):
        if user is not None and user not in self.users:
            self.users.append(user)

    def insert_followers(self, followers: List[Follower]):
        if followers is not None and followers not in self.followers:
            self.followers.extend(followers)

    def insert_tweet(self, tweet: Tweet):
        if tweet is not None and tweet not in self.tweets:
            self.tweets.append(tweet)

    def insert_hashtags(self, hashtags: List[Hashtag]):
        if hashtags is not None and hashtags not in self.hashtags:
            self.hashtags.extend(hashtags)

    def insert_mentions(self, mentions: List[Mention]):
        if mentions is not None and mentions not in self.mentions:
            self.mentions.extend(mentions)

    def insert_retweet(self, retweet: Retweet):
        if retweet is not None and retweet not in self.retweets:
            self.retweets.append(retweet)

    def insert_likes(self, likes: List[Like]):
        if likes is not None and likes not in self.likes:
            self.likes.extend(likes)

    # --- SEARCH

    def exists(self, clazz, key: int) -> bool:
        """Diz se um objeto existe numa coleção de acordo com seu tipo e ID"""
        return self.find_by_id(clazz, key) is not None

    def find_by_id(self, clazz, key: int) -> object:
        """Retorna um objeto de uma coleção se ele existir de acordo com seu tipo e ID"""
        if isinstance(clazz, User):
            return next((user for user in self.users if user.user_id == key), None)
        elif isinstance(clazz, Tweet):
            return next((tweet for tweet in self.tweets if tweet.tweet_id == key), None)
        else:
            return None
