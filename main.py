from ps.layout import MainWindow 
from PySide6.QtWidgets import QApplication
from query_spider.spiders.test_crawler import TestQuerySpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    process = CrawlerProcess(get_project_settings())
    process.crawl(TestQuerySpider)
    process.start()
    sys.exit(app.exec())

