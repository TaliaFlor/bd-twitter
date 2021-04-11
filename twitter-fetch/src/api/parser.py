import random
from typing import List

from faker import Faker

from src.api.collection import Collection
from src.models.follower import Follower
from src.models.hashtag import Hashtag
from src.models.like import Like
from src.models.mention import Mention
from src.models.retweet import Retweet
from src.models.tweet import Tweet
from src.models.user import User
from src.util.file import read_file
from src.util.number import randmedium


class Parser:
    """Parsers the data received from the API into the desired objects models"""

    def __init__(self, data):
        self.data = data
        self.collection = Collection()
        self.fake = Faker()

    # ------- PUBLIC METHODS  -------

    def parse(self) -> Collection:
        """
        Extrai as informações desejadas dos dados passados pela API.
        :return: um objeto com as coleções dos dados extraídos
        """
        posts = self.data["statuses"]
        for post in posts:
            self.collection.insert_user(self.__parse_user(post))

            content = post["text"]
            if content[:4] == "RT @":
                self.collection.insert_retweet(self.__parse_retweet(post))
            else:
                self.__parse_post(post)

        self.collection.insert_followers(self.__generate_followers())
        self.collection.insert_likes(self.__generate_likes())

        return self.collection

    # ------- PRIVATE METHODS  -------

    def __parse_user(self, post) -> User:
        json = post["user"]
        return User(
            user_id=json["id"],
            email=self.fake.free_email(),
            password=self.fake.password(),
            username=json["screen_name"],
            display_name=json["name"],
            location=json["location"],
            description=json["description"],
            verified=json["verified"],
            joined_on=json["created_at"]
        )

    def __parse_retweet(self, post) -> Retweet:
        retweet = Retweet(
            tweet_id=post["retweeted_status"]["id"],
            user_id=post["user"]["id"],
            retweeted_on=post["created_at"]
        )

        if not self.collection.exists(retweet.tweet_id):
            self.__parse_post(post["retweeted_status"])

        user_id = post["retweeted_status"]["user"]["id"]
        if not self.collection.exists(user_id):
            self.collection.insert_user(self.__parse_user(post["retweeted_status"]))

        return retweet

    def __parse_post(self, post):
        """Parsers a post. Can be a tweet, a quote or a reply"""
        self.collection.insert_tweet(self.__parse_tweet(post))
        self.collection.insert_hashtags(self.__parse_hashtags(post))
        self.collection.insert_mentions(self.__parse_mentions(post))

        if post["is_quote_status"] == True and not self.collection.exists(post["quoted_status"]["id"]):
            self.__parse_post(post["quoted_status"])

    @staticmethod
    def __parse_tweet(post) -> Tweet:
        quote_id = post["quoted_status_id"] if post["is_quote_status"] == True else None
        return Tweet(
            tweet_id=post["id"],
            user_id=post["user"]["id"],
            reply_id=post["in_reply_to_status_id"],
            quote_id=quote_id,
            content=post["text"],
            posted_on=post["created_at"]
        )

    @staticmethod
    def __parse_hashtags(post) -> List[Hashtag]:
        hashtags = []
        tweet_id = post["id"]
        json = post["entities"]["hashtags"]
        for item in json:
            hashtag = Hashtag(
                tweet_id=tweet_id,
                hashtag=item["text"]
            )
            hashtags.append(hashtag)

        return hashtags

    def __parse_mentions(self, post) -> List[Mention]:
        mentions = []
        tweet_id = post["id"]
        json = post["entities"]["user_mentions"]
        for item in json:
            mention = Mention(
                tweet_id=tweet_id,
                user_id=item["id"]
            )
            mentions.append(mention)

            if not self.collection.exists(mention.user_id):
                self.collection.insert_user(self.__parse_user_from_mentions(item))

        return mentions

    def __parse_user_from_mentions(self, user_mention) -> User:
        return User(
            user_id=user_mention["id"],
            email=self.fake.free_email(),
            password=self.fake.password(),
            username=user_mention["screen_name"],
            display_name=user_mention["name"]
        )

    def __generate_followers(self) -> List[Follower]:
        """Generates random followers to a random number of users"""
        sample_size = randmedium(self.collection.users)
        users = random.sample(self.collection.users, sample_size)

        followers = []
        for user in users:
            followers.extend(self.__assign_followers_to_a_user(user))
        return followers

    def __assign_followers_to_a_user(self, user: User):
        """Assign a random number of followers to a single user"""
        sample_size = randmedium(self.collection.users)
        users = random.sample(self.collection.users, sample_size)

        followers = []
        for user_follower in users:
            follower = Follower(
                following_id=user_follower.user_id,
                user_id=user.user_id
            )
            followers.append(follower)

        return followers

    def __generate_likes(self) -> List[Like]:
        """Generates random likes to a random number of tweets"""
        sample_size = randmedium(self.collection.tweets)
        tweets = random.sample(self.collection.tweets, sample_size)

        likes = []
        for tweet in tweets:
            likes.extend(self.__assign_likes_to_a_tweet(tweet))
        return likes

    def __assign_likes_to_a_tweet(self, tweet: Tweet):
        """Assign a random number of likes to a single tweet"""
        sample_size = randmedium(self.collection.users)
        users = random.sample(self.collection.users, sample_size)

        likes = []
        for user in users:
            like = Like(
                tweet_id=tweet.tweet_id,
                user_id=user.user_id
            )
            likes.append(like)

        return likes


if __name__ == "__main__":
    data = read_file("../../resources/examples/sample_response.json")

    parser = Parser(data)
    collection = parser.parse()

    # print(collection.users)
    # print(collection.retweets)
    # print(collection.tweets)
    # print(collection.hashtags)
    # print(collection.mentions)
    # print(collection.followers)
    # print(collection.likes)
