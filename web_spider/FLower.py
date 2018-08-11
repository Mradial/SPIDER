#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-08-08 08:24:03
# Project: Flower

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.aihuhua.com/baike/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.title >li > a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.two_page)

    @config(priority=5)
    def two_page(self, response):
        for each in response.doc(' .title > a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.three_page)
        # if  response.doc('.page> li>a:contain(下一页)'):
        #     self.crawl(response.doc('.page>li>a:contain(下一页)').items().attr.href, callback=self.detail_page)

    @config(priority=5)
    def three_page(self, response):
        for each in response.doc(' .title > a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)
        # if  response.doc('.page> li>a:contain(下一页)'):
        #     self.crawl(response.doc('.page>li>a:contain(下一页)').items().attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }

