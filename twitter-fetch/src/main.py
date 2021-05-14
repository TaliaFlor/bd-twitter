from modules.twitter_exporter import TwitterExporter
from modules.twitter_fetcher import TwitterFetcher
from modules.twitter_parser import TwitterParser

config_file = "../resources/config.json"
data_folder = "../../sql/data/"

data_amount = {"count": 100, "page": 10}  # 100 * 10 = 1000
try:
    print('===== App initialized =====')

    fetcher = TwitterFetcher(config_file, data_amount=data_amount)
    posts = fetcher.fetch()

    parser = TwitterParser(posts)
    collection = parser.parse()

    exporter = TwitterExporter(data_folder, collection)
    exporter.export()

    print('===== App finalized =====')
except Exception as exp:
    raise exp
