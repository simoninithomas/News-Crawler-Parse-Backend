import datetime

import scrapy
from NewsCrawlBot.items import ChallengesItem


class ChallengesSpider(scrapy.Spider):
    name = "Challenges"
    allowed_domains = ["http://www.challenges.fr/"]
    start_urls = [
        "http://www.challenges.fr/",
    ]

    def parse(self, response):
        time = datetime.datetime.now()
        for sel in response.xpath('//article'):
            item = ChallengesItem()
            item['language'] = "FR"
            item['title'] = sel.xpath('header/h2/a/text()').extract_first(default='')
            item['publisher'] = "Challenges"
            item['publishedDate'] = "time" #sel.xpath('pubDate/text()').extract_first(default='')
            item['url'] = "http://www.challenges.fr" + sel.xpath('header/h2/a/@href').extract_first(default='')
            item['image'] = sel.xpath('a/img/@class').extract_first(default='http://referentiel.nouvelobs.com/logos/og/logo-challa.jpg')
            item['theme'] = 'Economie' #sel.xpath('ul/li[@class="tag"]/a/text()').extract_first(default='')
            yield item



