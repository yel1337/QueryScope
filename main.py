from PySide6.QtWidgets import QApplication
from scrapy.utils.project import get_project_settings
from twisted.internet import asyncioreactor
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import sys

from query_spider.spiders.test_crawler import TestQuerySpider
from ps.layout import MainWindow

scraped_items = []

class CollectorPipeline:
    def process_item(self, item, spider):
        scraped_items.append(item)
        return item

@defer.inlineCallbacks
def crawl_and_start_gui():
    configure_logging()
    runner = CrawlerRunner(settings={
        'ITEM_PIPELINES': {
            '__main__.CollectorPipeline': 1
        }
    })

    yield runner.crawl(TestQuerySpider)

    # Crawl finished — now start the GUI
    app = QApplication(sys.argv)

    if scraped_items:
        print("Scraped:", scraped_items[0].get('scraped_data'))
        item_data = scraped_items
    else:
        print("No scraped data found.")
        item_data = []

    window = MainWindow(item_data, spider_instance=None)
    window.show()
    app.exec()

    reactor.stop()

def initialize_application():
    reactor.callWhenRunning(crawl_and_start_gui)
    reactor.run()

if __name__ == "__main__":
    initialize_application()

