#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-08-07 16:58:56
# Project: Read_en

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.enread.com/story/index.html', callback=self.two_page)
    # #首页解析
    # @config(age=10 * 24 * 60 * 60)
    # def index_page(self, response):
    #     for each in response.doc('.menu a[href^="http"]').items():
    #         if len(each.attr.href)<23 and "bookshop" in each.attr.href and "tngroom" in each.attr.href:
    #             pass
    #         else:
    #             self.crawl(each.attr.href, callback=self.two_page)
    # 二级页面解析
    @config(priority=2)
    def two_page(self, response):
        for each in response.doc('.title > a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.three_page)
        # return {
        #     "url": response.url,
        #     "title": response.doc('title').text(),
        # }
    # 三级详情界面解析
    @config(priority=2)
    def three_page(self, response):
        for each in response.doc('.list > .node_list > a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)
        # if  response.doc('.page> li>a:contain(下一页)'):
        #     self.crawl(response.doc('.page>li>a:contain(下一页)').items().attr.href, callback=self.detail_page)
    # 详情内容解析
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('#main >tr:first-child').text(),
            "content": response.doc('#dede_content').text(),
        }