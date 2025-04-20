import requests
from test.collect import Results 

class Http:
    def __init__(self, results: Results):
        self.url = results.url
        self.query = results.request_query
        self.payload_dict = dict()

    def _pass_payload(self):
        pass

    def sort_url(self):
        self.payload_dict["url"] = self.url
        protocol_end_index = data_dict["url"].find("://")

        if protocol_end_index != -1:
            data_dict["protocol"] = data_dict["url"][:protocol_end_index]
            domain_start_index = protocol_end_index + 3

            domain_end_index = data_dict["url"].find("/", domain_start_index)

            if domain_end_index != -1:
                data_dict["domain"] = data_dict["url"][domain_start_index:domain_end_index]
            else:
                data_dict["domain"] = data_dict["url"][domain_start_index:]

            path_start_index = domain_end_index + 1
            path_end_index = data_dict["url"].find("?", path_start_index)

            if path_end_index != -1:
                data_dict["path"] = data_dict["url"][path_start_index:path_end_index]
            else:
                data_dict["path"] = data_dict["url"][path_start_index]

            query_start_index = path_end_index + 1
            query_end_index = data_dict["url"].find("=", query_start_index)

            if query_end_index != -1:
                data_dict["query"] = data_dict["url"][query_start_index:query_end_index]
            else:
                data_dict["query"] = data_dict["url"][query_start_index]
            
            value_start_index = query_end_index + 1
            value_end_index = data_dict["url"].find("", value_start_index)

            if value_end_index != -1:
                data_dict["value"]= data_dict["url"][value_start_index:value_end_index]
            else:
                data_dict["value"] = data_dict["url"][value_start_index]

    def _get_sort(self, element):
        return self.payload_dict[element][0]

    def do_request(self):
        get_request = requests.get(f"{self.url}, params={self._pass_payload}")
        return get_request

    def request_status_code(self) -> int:
        with_get = self.do_request

        return with_get.status_code





