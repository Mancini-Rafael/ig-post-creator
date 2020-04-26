from scrapper.scrapper.spiders import fashion
from scrapy.crawler import CrawlerProcess
import os

class Main:
  def __init__(self):
    self.process = CrawlerProcess(settings={
      "FEEDS": {
          "items.json": {"format": "json"},
      },
    })

  def scrape(self):
    """
      Will generate a items.json file containing all the
      scrapped information. The scrapped information contains
      the image of the products, price, and payment options
    """
    if os.path.exists("items.json"):
      print("Deleting previous items")
      os.remove("items.json")
    else:
      print("The file does not exist, starting scrape")
    self.process.crawl(fashion.FashionSpider)
    self.process.start()