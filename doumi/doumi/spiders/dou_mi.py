# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from doumi.items import DoumiItem


class DouMiSpider(scrapy.Spider):
    name = 'dou_mi'
    allowed_domains = ['doumi.com']
    root_url="https://www.doumi.com"
    start_urls =["https://www.doumi.com/xa/"]

    def parse(self, response):
        link_pool = response.xpath('//div[@class="filter-cate-content"]/ul/li/a/@href').extract()
        for i in link_pool:
            # print(i)
            yield Request(self.root_url + i, callback=self.url_two_parse)

    def url_two_parse(self, response):
        link_pool = response.xpath("//h3/a[@target='_blank']/@href").extract()
        for i in link_pool:
            # print(i)
            yield Request(self.root_url + i, callback=self.url_three_parse)
        nxt=response.xpath('//a[@class="next"]/@href').extract()
        if nxt:
            yield Request(self.root_url + nxt, callback=self.url_three_parse)
        else:
            pass
    def url_three_parse(self,response):
        m = ItemLoader(item=DoumiItem(), response=response)
        m.add_xpath( "name",'//div[@class="clearfix"]/h2/text()')
        m.add_xpath('price','//span[@class="fl salary-num"]/b/text()')
        m.add_xpath('price_fun','//span[@class="fl salary-num"]/text()')
        m.add_xpath('price_fal','//div[@class="salary-tips"]/span[1]/text()')
        m.add_xpath('demain','//div[@class="salary-tips"]/span[2]/text()')
        m.add_xpath('order','//p[@data-name="contentBox"]/text()')
        m.add_xpath('location','//div[@class="jz-d-area"]/text()')
        return m.load_item()



