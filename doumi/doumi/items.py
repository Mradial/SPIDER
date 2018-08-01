# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class DoumiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    price_fun = scrapy.Field()
    price_fal = scrapy.Field()
    demain = scrapy.Field()
    number = scrapy.Field()
    order = scrapy.Field()
    location = scrapy.Field()
    # pass
