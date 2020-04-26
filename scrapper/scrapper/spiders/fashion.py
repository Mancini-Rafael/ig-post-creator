# -*- coding: utf-8 -*-
import scrapy


class FashionSpider(scrapy.Spider):
    name = 'fashion'
    '''
    urls = ['https://www.brechoclosetdeluxo.com.br/acessorios/',
            'https://www.brechoclosetdeluxo.com.br/acessorios/page/2/',
            'https://www.brechoclosetdeluxo.com.br/acessorios/page/3/',
            'https://www.brechoclosetdeluxo.com.br/acessorios/page/4/',
            'https://www.brechoclosetdeluxo.com.br/acessorios/page/5/',
            'https://www.brechoclosetdeluxo.com.br/roupas/',
            'https://www.brechoclosetdeluxo.com.br/bolsas/',
            'https://www.brechoclosetdeluxo.com.br/calcados/',
            'https://www.brechoclosetdeluxo.com.br/viagem/',
            'https://www.brechoclosetdeluxo.com.br/unissex/',
            'https://www.brechoclosetdeluxo.com.br/nunca-usados/',
            'https://www.brechoclosetdeluxo.com.br/sale/',
            'https://www.brechoclosetdeluxo.com.br/eletronicos/',
            'https://www.brechoclosetdeluxo.com.br/sale1/',
            'https://www.brechoclosetdeluxo.com.br/sale-gucci1/']
    '''

    def start_requests(self):
        urls = ['https://www.brechoclosetdeluxo.com.br/acessorios/',
                'https://www.brechoclosetdeluxo.com.br/acessorios/page/2/',
                'https://www.brechoclosetdeluxo.com.br/acessorios/page/3/',
                'https://www.brechoclosetdeluxo.com.br/acessorios/page/4/',
                'https://www.brechoclosetdeluxo.com.br/acessorios/page/5/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        items_info = []
        for item_container in response.css("div.item"):
            url = item_container.css("div.item-image-container img::attr(data-srcset)").get().split(sep=" ")[-2].replace("//", "")
            desc = item_container.css("div.item-info-container a::attr(title)").get()
            value_raw = item_container.css("div.item-info-container span.item-price::text").get().strip()
            installment_info_raw = dict(allowed_installments= item_container.css("span.installment-amount::text").get(),
                                        installment_price= item_container.css("span.installment-price::text").get())
            installment_info = "{ai}X de {ip} sem juros".format(ai = installment_info_raw["allowed_installments"],
                                                                ip = installment_info_raw["installment_price"])
            transfer_info = "{info} (-10% TRANSFERÊNCIA)".format(info = item_container.css("p.price-sale-vk span::text").get())
            items_info.append(dict(url=url, desc=desc, value_raw=value_raw, installment_info=installment_info, transfer_info=transfer_info))
        
        # Used in debug mode
        # for item_info in items_info:
        #     print(item_info)
        
        return items_info
