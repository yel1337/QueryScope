"""
Each of test cases requires data(scraped content) from item via pipeline or alternative
and a query must met the requirements for each of the test.

If for example eg. query#1 doesn't have a parameter and test_case#1 requires a query to
have one then the current test will fail.
"""

from query_spider.items import QueryScrapyItem

try:
    QueryScrapyItem
except NameError as e:
    f"{e}"

class CollectorPipeline:
    def __init__(self):
        self.DataFromItem = []

    def process_item(self, item, spider):
        scraped_items.append(item)
        return item

from scrapy.crawler import CrawlerRunner

def crawl_and_start_gui():
    runner = CrawlerRunner(settings={
        'ITEM_PIPELINES': {
            '__main__.CollectorPipeline': 1
        }
    })

from exceptions.test_exceptions import NoDataErrorFromPipeline
from test.validate import Validate

class Cases:
    def __init__(self, data_from_collector):
        self.ItemInstance = QueryScrapyItem()
        self.CollectorInstance = CollectorPipeline()
        """
        Collect data from Collector Pipeline - This holds the scraped datas
        from item via a pipeline.
        """
        self.data_from_collector = data_from_collector
        self.signal = None

        """
        Number of results will be stored in this dictionary
        """
        self.results {
            "pass": 0,
            "fail": 0
        }

        if self.data_from_collector is not None:
            self.signal = True
        else:
            self.signal = False
            raise NoDataErrorFromPipeline

    def _test_one(self, signal):
        """
        Test the result if it contains parameter indicators otherwise will fail the test
        """
        len_of_set = len(self.data_from_collector)
        required_string = ["?", "="]
        if signal:
            for data in range(len_of_set):
                len_of_data = len(data)
                # This will goes for each of every character of the set 
                for character in range(len_of_data):
                    if character == required_string[0] and character[range(len_of_data+1)]:
                        return True

                        break 
                    elif character == required_string[0] and character[range(len_of_data+1)]:
                        return False

                       break

    @property 
    def _collect_result(self):
        yield self.results {
            "pass": self.result_pass,
            "fail": self.result_fail
        }
    
    def count_result(self):
        """
        Collect the results from each of the test cases and pass it to the validator
        """
        suites = [_test_one] # Planned: [_test_one, _test_two, _test_three, _test_...]
        results = [func() for func in suites]

        for result in enumerate(results):
            if result:
                self.result_pass += 1
            elif not result:
                self.result_fail += 1

            break

    def pass_to_validator(self):
        value_for_validator = yield self._collect_result
        
        return value_for_validator



