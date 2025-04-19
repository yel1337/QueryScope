"""
This is were the validations of gathered required scraped items from test module
are kept. 

# Deprecated Plan
Planned workaround would be:
    [test spider.parse] -> [test item]-> [test_module.checklist] -> [matplotlib graph]

# Current
Planned workaround would be:
    {test_case_1,   
     test_case_2,
     test_case_3,   # This is a set of test cases the query will undergo 
     test_case_4,
     test_case_5
    }

    [set_of_test_cases] -> collector() -> validator() -> to GUI 

Each test url from [query_spider.resources.test_urls] has a test case and each of
query is expected to scrape the test cases to pass the initial test.

To add, each of test cases are differentiated by its difficulty to be scrape
using queries. If the query find it difficult or were not able to get the test case 
then it easy to tell that it did failed the test. 
"""

from test.test_case.suites import Cases
from exceptions import TypeError
from test.collect import Results
import logging

class Validate:
    def __init__(self, value_from_setter):
        self.results_iterator = value_from_setter
        # Enable Logging
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(message)s')
        self.logger = logging.getLogger("ClassLogger")

    RETURN_WITH_DATA = 0
    RETURN_WITHOUT_DATA = 1
    RETURN_WITH_ERROR = 2
    
    def _if_str(self, data):
        return isinstance(data, int)
    
    def _if_not(self, data):
        try:
            if not self._if_str(data):
                raise TypeError
            return RETURN_WITH_DATA
        except TypeError as e:
            self._error_message = str(e)
            return RETURN_WITH_ERROR

    def log_type(self, data):
        result = self._if_not(data)
        if result == RETURN_WITH_DATA:
            self.logger.info("Results set received")
        else if self._if_not == RETURN_WITH_ERROR: 
            self.logger.error(f"Results set encountered an error during validating. "
                              f"Reason: {self._error_message}")
        else if self.results_iterator == None:
            self.logger.error(f"Results set are empty")

    def _to_result(self):
        instance_of_result = Results()
        value_to_be_pass = self.results_iterator.pass_to_validator()

        return value_to_be_pass

    




    

    

    





 