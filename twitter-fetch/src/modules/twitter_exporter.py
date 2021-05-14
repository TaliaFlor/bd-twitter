from src.models.follower import Follower
from src.models.hashtag import Hashtag
from src.models.like import Like
from src.models.mention import Mention
from src.models.retweet import Retweet
from src.models.tweet import Tweet
from src.models.user import User
from src.util.clazz import get_attributes
from src.util.collection import Collection
from src.util.file import write_file


class TwitterExporter:
    """Exports the data parsed into the collection"""

    def __init__(self, data_folder, collection: Collection):
        self.data_folder = data_folder
        self.collection = collection

    def __get_export_tuples(self):
        """Returns a list with tuples of the data stored in this class to be used in the export"""
        return [
            (User, "users", self.collection.users),
            (Follower, "followers", self.collection.followers),
            (Tweet, "tweets", self.collection.tweets),
            (Hashtag, "hashtags", self.collection.hashtags),
            (Mention, "mentions", self.collection.mentions),
            (Retweet, "retweets", self.collection.retweets),
            (Like, "likes", self.collection.likes)
        ]

    def export(self):
        """Exports the data to CSVs files"""
        print('--- Exporting data')
        for index, data_tuple in enumerate(self.__get_export_tuples(), start=1):
            headers = get_attributes(data_tuple[0])
            write_file(
                f"{self.data_folder}{index}-load_{data_tuple[1]}.csv",  # "{path}1-load_users.csv"
                data_tuple[2],
                header=headers
            )
