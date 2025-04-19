from test.checklist import Test
from query_spider.items import QueryScrapyItem
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

        with open(self.url_resource, "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
        
        self.start_urls = urls
        self.test_query = "//link[@rel='stylesheet']/@href"
    
    def start_requests(self):
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            "Referer": "https://www.google.com/", 
            "Accept-Encoding": "identity;   q=1, *;q=0",
            "Range": "bytes=0-",
        }
        yield scrapy.Request(
            url="https://www.nytimes.com/",
            headers=headers,
            callback=self.parse
        )

    
    def parse(self, response):
        results = response.xpath(self.test_query).get()

        item = QueryScrapyItem()
        item['scraped_data'] = results
        yield item 