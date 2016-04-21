import datetime

import scrapy
from NewsCrawlBot.items import EclaireusesItem


class EclaireusesSpider(scrapy.Spider):
    name = "Eclaireuses"
    allowed_domains = ["www.leseclaireuses.com/"]
    start_urls = [
        "http://www.leseclaireuses.com/",
    ]

    def parse(self, response):
        time = datetime.datetime.now()
        for sel in response.xpath('//div[@class="article"]'):
            item = EclaireusesItem()
            item['language'] = "FR"
            item['title'] = sel.xpath('a/@title').extract_first(default='')
            item['publisher'] = "Les Eclaireuses"
            item['publishedDate'] = "time"
            item['url'] = sel.xpath('a/@href').extract_first(default='')
            item['image'] = sel.xpath('a/img/@src').extract_first(default='http://www.leseclaireuses.com/wp-content/themes/simplemag/images/logo.png')
            item['theme'] = 'Mode' #sel.xpath('ul/li[@class="tag"]/a/text()').extract_first(default='')
            yield item
