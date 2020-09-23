# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UfcscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    nick_name = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    reach = scrapy.Field()
    stance = scrapy.Field()
    date_birth = scrapy.Field()
    record = scrapy.Field()
    SLpm = scrapy.Field()
    StrAcc = scrapy.Field()
    SApm = scrapy.Field()
    StrDef = scrapy.Field()
    TDavg = scrapy.Field()
    TDacc = scrapy.Field()
    TDdef = scrapy.Field()
    SubAvg = scrapy.Field()