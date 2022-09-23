# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    name = scrapy.Field()
    shop = scrapy.Field()
    icons = scrapy.Field()
    link = scrapy.Field()
    has_pro = scrapy.Field()
    weight = scrapy.Field()
    brand = scrapy.Field()
    ram = scrapy.Field()
    series = scrapy.Field()
    disk = scrapy.Field()
    cpu = scrapy.Field()
    category = scrapy.Field()

