from test.validate import Validate
from dataclasses import dataclass
from ps.layout import MainWindow

@dataclass
class Results:
    def __init__(self):
        """
        Results from test should be kept here and pass along with getters

        These can be exported to json format or any supported types for
        reference
        """
        xpath_query: str = self.input_field
        result_pass: int = None 
        result_fail: int = None
