class TestError(Exception):
    pass

class NoDataError(TestError):
    def __init__(self, message="No data were scraped."):
        self.message = message
        super().__init__(f"{message}")