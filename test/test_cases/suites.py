"""
Each of test cases requires data(scraped content) from item via pipeline or alternative
and a query must met the requirements for each of the test.

If for example eg. query#1 doesn't have a parameter and test_case#1 requires a query to
have one then the current test will fail.
"""

from query_spider.items import QueryScrapyItem
import sys

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
from http import Http
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

        self.http_request = Http()

        """
        Number of results will be stored in this dictionary
        """
        self.results {
            "pass": 0,
            "fail": 0
        }

        if self.data_from_collector is not None:
            return self.signal = True
        else:
            return self.signal = False
            raise NoDataErrorFromPipeline
            sys.exit(0)

    def _data_len(self, data: str) -> int: 
        data = self.data_from_collector 
        return len(data)
    
    def _parameter_indicators(self, index) -> int:
        indicators = ["?", "="]
        return indicators(index)

    # This method will be use throughout the code as a sort of signal for two result values
    def _result_signal(self, result_signal: int) -> bool:
        result_passed = True
        result_failed = False

        if isinstance(result_signal, int):
            if result_signal == 1:
                return result_passed
            elif result_signal == 0:
                return result_failed
        else:
            raise TypeError(f"TypeError: Only accepts int for {result_signal}!")        

    def _test_one(self) -> bool:
        """
        # Test the result if it contains parameter indicators otherwise will fail the test
        
        ### Example of scraped data with parameter indicators: 
            (https//:www.example.com/search?=) where "?" and "=" are parameter indicators   
        """
        if self.signal:
            for data in range(_data_len):
                # This will goes for each of every character of the set 
                for character in range(len_of_data):
                    if character == self._parameter_indicators[0] and character[range(_data_len+1)]:
                        return self._result_signal(1)

                        break 
                    elif character == self._parameter_indicators[0] and character[range(_data_len+1)]:
                        return self._result_signal(0)

                       break
    
    def _test_two(self) -> bool:
        """
        This Second Test Case will ensure the url along with the query will return 200
        if not then it will return status code 401 indicating the query along with the 
        url didn't work as it supposed to. 
        """
        self.http_request.do_request()
        
        if self.http_request.request_status_code == 200:
            return self._result_signal(1)
        elif self.http_request.request_status_code == 401:
            return self._result_signal(0)
 
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