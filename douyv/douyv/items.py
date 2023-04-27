# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 主播名
    nickname = scrapy.Field()
    # 图片
    verticalSrc = scrapy.Field()
