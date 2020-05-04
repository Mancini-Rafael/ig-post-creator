import os
from scrapy.crawler import CrawlerProcess
from scrapper.scrapper.spiders import fashion


class Main:
    def __init__(self):
        self.process = CrawlerProcess(settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        })

    def scrape(self, url):
        """
          Will generate a items.json file containing all the
          scrapped information from the url provided. The scrapped 
          information contains the image of the products, price, 
          and payment options
        """
        if os.path.exists("items.json"):
            print("Deleting previous items")
            os.remove("items.json")
        else:
            print("The file does not exist, starting scrape")
        print(f"************ Scraping: {url} ************")
        self.process.crawl(fashion.FashionSpider, url=url)
        self.process.start()
