from ps.layout import MainWindow
import scrapy
import os

class TestQuerySpider(scrapy.Spider):
    name = "test_query_spider"

    def __init__(self, *args, **kwargs):
        # Load the url resource for test case
        super().__init__(*args, **kwargs)
        self.url_resource = os.path.join(
            os.path.expanduser("~"), 
            "QueryScope/query_spider/spiders/resources/test_urls.txt"
        )
        self.test_query = self.load_test_query()

    def load_test_query(self, query):
        from_pyside = MainWindow()
        from_pyside.input_field.text()
        query = "//meta[@property='og:url' and contains(@content, 'search?query=')]/@content"

        return query
        # return from_pyside.input_field.text()

    def start_requests(self):
        with open(self.url_resource, "r") as f:
            start_urls = [line.strip() for line in f.readlines() if line.strip()]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        results = response.xpath(self.test_query).getall()
        yield {
            "scraped_data": results
        }