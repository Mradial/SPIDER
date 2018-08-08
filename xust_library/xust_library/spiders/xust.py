# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from xust_library.items import XustLibraryItem
from  pyquery import PyQuery as pq

class PythonBookSpider(scrapy.Spider):
    name = 'xust'
    llowed_domains = ['61.150.69.38']
    root_url="http://61.150.69.38:8080/opac/"
    class_pool=list("ABCDEFGHIJKNOPQRSTUVXZ")
    base_url="http://61.150.69.38:8080/opac/openlink.php"
    # url_query="http://61.150.69.38:8080/opac/openlink.php?strSearchType=coden&match_flag=forward&historyCount=1&strText={}&doctype=ALL&with_ebook=on&displaypg=100&showmode=list&sort=CATA_DATE&orderby=desc&dept=ALL"
    # start_urls = ["http://61.150.69.38:8080/opac/openlink.php?strSearchType=coden&match_flag=forward&historyCount=1&strText={}&doctype=ALL&with_ebook=on&displaypg=100&showmode=list&sort=CATA_DATE&orderby=desc&dept=ALL".format(j) for j in class_pool]
    start_urls = [
        "http://61.150.69.38:8080/opac/openlink.php?strSearchType=coden&match_flag=forward&historyCount=1&strText={}&doctype=ALL&with_ebook=on&displaypg=15&showmode=list&sort=CATA_DATE&orderby=desc&dept=ALL".format("A")]

    def parse(self, response):
        link_pool=response.xpath('//li/h3/a/@href').extract()
        for i in link_pool:
            yield Request(self.root_url+i,callback=self.link_parse)
        if len(response.css(".pagination a::text").extract())>=1:
            yield Request(self.base_url + response.css(".pagination a::attr(href)").extract()[-1], callback=self.parse)
        else:
            print("你是煞笔吗")
    def link_parse(self,response):
        m = ItemLoader(item=XustLibraryItem(), response=response)
        m.add_xpath( 'book_name', '//*[@id="item_detail"]/dl[1]/dd/a/text()')
        m.add_xpath( 'book_press', '//*[@id="item_detail"]/dl[2]/dd/text()')
        # #m.add_xpath( 'book_wenzhai', '//*[@id="item_detail"]/dl[10]/dd/text()')
        # m.add_xpath( 'book_douban', '//*[@id="intro"]/text()')
        # # m.add_xpath( 'book_date', '//*[@id="item_detail"]/dl[1]/dd/text()')
        m.add_xpath( 'book_frequency', '//*[@id="marc"]/text()',re="[0-9]+")
        return m.load_item()


