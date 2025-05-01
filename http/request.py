import requests
from test.collect import Results 

class Http:
    def __init__(self, results: Results):
        self.url = results.url
        self.query = results.request_query
        self.payload_dict = dict()

    def _pass_payload(self) -> dict:
        return {
            self.payload_dict["query"][0],
            self.payload_dict["value"][0]
        }

    def sort_url(self):
        self.payload_dict["url"] = self.url
        protocol_end_index = self.payload_dict["url"].find("://")

        if protocol_end_index != -1:
            self.payload_dict["protocol"] = self.payload_dict["url"][:protocol_end_index]
            domain_start_index = protocol_end_index + 3

            domain_end_index = self.payload_dict["url"].find("/", domain_start_index)
        if domain_end_index != -1:
            self.payload_dict["domain"] = self.payload_dict["url"][domain_start_index:domain_end_index]
        else:
            self.payload_dict["domain"] = self.payload_dict["url"][domain_start_index:]
            return

        path_start_index = domain_end_index + 1
        query_start_index = self.payload_dict["url"].find("?", path_start_index)
        if query_start_index != -1:
            self.payload_dict["path"] = self.payload_dict["url"][path_start_index:query_start_index]
        else:
            self.payload_dict["path"] = self.payload_dict["url"][path_start_index:]
            return

        query_string = self.payload_dict["url"][query_start_index + 1:]
        if "=" in query_string:
            key, value = query_string.split("=", 1)
            self.payload_dict["query"] = key
            self.payload_dict["value"] = value

    def _get_sort(self, element: str):
        # By default index 0 or [0] is set as default
        return self.payload_dict[element][0]

    def do_request(self):
        if self._pass_payload is None:
            self._pass_payload = {}

        requests.get(f"{self.url}, params={self._pass_payload}")

    def request_status_code(self) -> int:
        with_get = self.do_request

        return with_get.status_code





