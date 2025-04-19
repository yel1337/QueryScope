"""
This is were the validations of gathered required scraped items from test module
are kept. 

Planned workaround would be:
    [test spider.parse] -> [test item]-> [test_module.checklist] -> [matplotlib graph]

Each test url from [query_spider.resources.test_urls] has a test case and each of
query is expected to scrape the test cases to pass the initial test.

To add, each of test cases are differentiated by its difficulty to be scrape
using queries. If the query find it difficult or were not able to get the test case 
then it easy to tell that it did failed the test. 
"""

from exceptions.test_exceptions import NoDataError
from query_spider.items import QueryScrapyItem
import scrapy

class Test:
    def __init__(self):
        super().__init__()

    def to_mp_graph(self, data):
        if self.check(data):
            return self.check(data)
        else:
            raise NoDataError

    def check(self, datas):
        test_cases = [
            {"nytimes": "https://g1.nyt.com/fonts/css/web-fonts.c851560786173ad206e1f76c1901be7e096e8f8b.css"}
        ]

        if datas == test_cases[0]["nytimes"]:
            return f"test query did passed the test!"
        else:
            return f"test query did NOT passed the test!"