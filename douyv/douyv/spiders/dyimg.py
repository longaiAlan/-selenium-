import json

import scrapy
from douyv.items import DouyvItem


class DyimgSpider(scrapy.Spider):
    name = 'dyimg'
    allowed_domains = ['douyu.com']
    # start_urls = ['http://douyv.com/']
    url = 'https://m.douyu.com/api/room/list?page={}&type=yz'
    offset = 1
    start_urls = [url.format(offset)]

    def parse(self, response):
        datas = json.loads(response.text)['data']['list']
        for data in datas:
            item = DouyvItem()
            item['nickname'] = data['nickname']
            item['verticalSrc'] = data['verticalSrc']
            yield item
        self.offset += 1
        yield scrapy.Request(self.url.format(self.offset), callback=self.parse)
