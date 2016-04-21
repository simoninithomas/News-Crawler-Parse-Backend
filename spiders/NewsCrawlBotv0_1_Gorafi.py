import datetime

import scrapy
from NewsCrawlBot.items import GorafiItem


class GorafiSpider(scrapy.Spider):
    name = "Gorafi"
    allowed_domains = ["www.legorafi.fr/"]
    start_urls = [
        "http://www.legorafi.fr/",
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="articles"]/article'):
            time = datetime.datetime.now()
            item = GorafiItem()
            item['language'] = "FR"
            item['title'] = sel.xpath('h2/a/text()').extract_first(default='')
            item['publisher'] = "Le Gorafi"
            item['publishedDate'] = "time"
            item['url'] = sel.xpath('h2/a/@href').extract_first(default='')
            item['image'] = sel.xpath('figure//img/@src').extract_first(default='')
            item['theme'] = "Humour"
            yield item

