from modules.exporter import Exporter
from modules.fetcher import Fetcher
from modules.parser import Parser

config_file = "./resources/config.json"
data_folder = "./../sql/data/"

data_amount = {"count": 100, "page": 10}  # 100 * 10 = 1000
try:
    print('===== App initialized =====')

    fetcher = Fetcher(config_file, data_amount=data_amount)
    posts = fetcher.fetch()

    parser = Parser(posts)
    collection = parser.parse()

    exporter = Exporter(data_folder, collection)
    exporter.export()

    print('===== App finalized =====')
except Exception as exp:
    raise exp
