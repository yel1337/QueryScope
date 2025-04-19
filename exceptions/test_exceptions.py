class TestError(Exception):
    pass

class NoDataErrorFromPipeline(TestError):
    def __init__(self, message="Error: No data in Item Pipeline"):
        self.message = message
        super().__init__(f"{message}")

class TypeError(Exception):
    def __init__(self, type_error_message="iterator must be an int"):
        self.message = message
        super().__init__(self.message)