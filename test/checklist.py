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

from query_spider.items import QueryScrapyItem
from exceptions.test_exceptions import NoDataError
import scrapy

class Test(QueryScrapyItem):
    test_scraped = scrapy.Field()

    def __init__(self):
        super().__init__() 
        item = QueryScrapyItem['scraped_data']

        self['test_scraped'] = item

    def to_mp_graph(self, value_from_test):
        if self.check:
            return value_from_test
        else:
            raise NoDataError

    def check(self):
        positive = 0

        test_cases = [
            {"nytimes": "https://www.nytimes.com/search?query="}
        ]

        for case in self['test_scraped']:
            if case == test_cases[0]:
                positive += 1
                
                return f"{positive}"
            else:
                return f"query did not get the test"