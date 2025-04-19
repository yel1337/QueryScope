from test.validate import Validate
from dataclasses import dataclass

@dataclass
class Results:
    def __init__(self):
        """
        Results from test should be kept here and pass along with getters

        These can be exported to json format or any supported types for
        reference
        """
        query: str = None
        result_pass: str = None
        result_fail: str = None
