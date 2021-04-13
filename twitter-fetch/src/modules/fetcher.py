from twitter import Twitter, OAuth

from src.util.file import read_file


class Fetcher:
    """Fetchs data from the Twitter API"""

    def __init__(self, config_file):
        """Authenticates to the Twitter API with the credentials provided in the file"""
        self.config = read_file(config_file)
        self.twitter = self.__get_twitter()

    def __get_twitter(self):
        credentials = self.config["twitter"]
        oauth = OAuth(
            token=credentials["token"],
            token_secret=credentials["token_secret"],
            consumer_key=credentials["consumer_key"],
            consumer_secret=credentials["consumer_secret"]
        )
        return Twitter(auth=oauth)

    def fetch(self):
        print('Fetch started')
        query = self.config["application"]["query"]

        posts = []
        next_token = ""
        while True:
            try:
                response = self.twitter.search.tweets(q=query + next_token)
                next_token = response["search_metadata"]["next_results"]
                posts.extend(response["statuses"])
                print(response)
            except Exception as exp:
                print(exp)
                break

        print('Fetch finalized')
        return posts
