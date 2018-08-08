# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XustLibraryItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    # book_date = scrapy.Field()
    book_press = scrapy.Field()
    # book_wenzhai = scrapy.Field()
    book_douban = scrapy.Field()
    book_frequency = scrapy.Field()
    # book_name = scrapy.Field()
    # book_name = scrapy.Field()