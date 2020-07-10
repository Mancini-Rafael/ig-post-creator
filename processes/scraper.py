import os
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapper.scrapper.spiders import fashion


class Main:
    def __init__(self):
        pass

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
        runner = CrawlerRunner()
        d = runner.crawl(fashion.FashionSpider, url=url)
        d.addBoth(lambda _: reactor.stop())
        reactor.run() # the script will block here until the crawling is finished
