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
    def __init__(self, scraped_data):
        super().__init__()
        self['scraped_data'] = scraped_data

    def to_mp_graph(self, value_from_test):
        if self.check:
            return value_from_test
        else:
            raise NoDataError

    def check(self):
        result_from_test = 0
        data = self['scraped_data']

        if not isinstance(data, (list, tuple)):
            data = [data]

        test_cases = [
            {"nytimes": "https://g1.nyt.com/fonts/css/web-fonts.d05a02583ca20b8afd5115f3ef8f1b8d134f743d.css"}
        ]

        for case in data:
            if case == test_cases[0]:
                result_from_test += 1
                
                return f"{result_from_test}"
            else:
                return f"query did not get the test"