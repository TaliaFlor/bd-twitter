import tweepy
from tweepy import API

from src.util.file import read_file


class Fetcher:
    """Fetchs data from the Twitter API"""

    def __init__(self, config_file, data_amount=None):
        """Authenticates to the Twitter API with the credentials provided in the file"""
        self.config = read_file(config_file)
        self.twitter = self.__get_twitter()

        if data_amount is None:
            data_amount = {"count": 15, "page": 1}
        self.data_amount = data_amount

    def __get_twitter(self) -> API:
        credentials = self.config["twitter"]
        auth = tweepy.OAuthHandler(
            consumer_key=credentials["consumer_key"],
            consumer_secret=credentials["consumer_secret"]
        )
        auth.set_access_token(
            key=credentials["token"],
            secret=credentials["token_secret"]
        )
        return tweepy.API(auth)

    def fetch(self) -> list:
        print('--- Fetching data')
        query = self.config["application"]["query"]

        data = []
        for page in tweepy.Cursor(self.twitter.search, q=query, lang="en", count=self.data_amount["count"]).pages(self.data_amount["page"]):
            data.extend(page)

        print(f'\t- {len(data)} data fetched')
        return data
