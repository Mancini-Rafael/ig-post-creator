# -*- coding: utf-8 -*-
import scrapy


class FashionSpider(scrapy.Spider):

    name = 'fashion'
    custom_settings = {
        'LOG_ENABLED': False,
    }

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        print(f"************ Parsing response ************")
        items_info = []
        for item_container in response.css("div.item"):
            has_no_stock = item_container.css(
                'div.item-image-container a.overlay-no-stock h4::text').get()
            desc = item_container.css(
                "div.item-info-container a::attr(title)").get()
            url = item_container.css(
                "div.item-image-container img::attr(data-srcset)").get().split(sep=" ")[-2].replace("//", "")
            value_raw = item_container.css(
                "div.item-info-container span.item-price::text").get().strip().replace(",00", "").replace("R$", "R$ ")
            if has_no_stock == 'Esgotado':
                print('Ignoring', desc, ' - Esgotado')
                continue
            else:
                print('Added', desc, ' - Disponível')
                items_info.append(
                    dict(url=url, desc=desc, value_raw=value_raw))
        print(f"************ Finished parsing response ************")
        return items_info
