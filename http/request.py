import requests
from test.collect import Results 

class Http:
    def __init__(self, results: Results):
        self.url = results.url
        self.query = results.query

    def _pass_payload(self):
        payload = {f'{self.query}'}
        return payload

    def do_request(self):
        get_request = requests.get(f"{self.url}, params={self._pass_payload}")
        return get_request

    def request_status_code(self) -> int:
        with_get = self.do_request

        return with_get.status_code





