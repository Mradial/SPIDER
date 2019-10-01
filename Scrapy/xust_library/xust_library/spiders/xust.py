# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from xust_library.items import XustLibraryItem

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
            yield Request(self.root_url+i+r"#marc_format",callback=self.link_parse)
        if len(response.css(".pagination a::text").extract())>=1:
            yield Request(self.base_url + response.css(".pagination a::attr(href)").extract()[-1], callback=self.parse)
        else:
            self.logger.debug("到此为止")
    def link_parse(self,response):
        item=XustLibraryItem()
        # item['book_url'] = response.url[-10:] #书籍链接标识码
        item['book_frequency'] = response.xpath('//*[@id="marc"]/text()').re("[0-9]+")[0] # 浏览次数
        item[ 'book_name'] =response.xpath('//*[@id="item_detail"]/dl[1]/dd/a/text()').extract_first() # 书名
        item['book_pub']=response.xpath('//*[@id="item_detail"]/dl[2]/dd/text()').extract_first() # 出版信息
        item['class_num'] = response.css(".whitetext").xpath("./td[1]/text()").extract_first()#中图法分类号
        item['num'] = len(response.css(".whitetext").xpath("./td[1]/text()"))#书籍数量
        item['now_num'] = len(response.css(".whitetext").xpath("./td").re('green'))# 可借数目
        return item


