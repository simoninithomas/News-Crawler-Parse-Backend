import datetime

import scrapy
from NewsCrawlBot.items import GameBlogItem


class GameBlogSpider(scrapy.Spider):
    name = "GameBlog"
    allowed_domains = ["gameblog.com"]
    start_urls = [
        "http://www.gameblog.fr/actualite.php",
    ]

    def parse(self, response):
        for sel in response.xpath('//article'):
            time = datetime.datetime.now()
            item = GameBlogItem()
            item['language'] = "FR"
            item['title'] = sel.xpath('div/a[@class="titre"]/text()').extract_first(default='')
            item['publisher'] = "GameBlog"
            item['publishedDate'] = "time"
            item['url'] = sel.xpath('div/a[@class="titre"]/@href').extract_first(default='')
            if item['url'].startswith('/'):
                item['url'] = "http://www.gameblog.fr" + item['url']
            item['image'] = "http://cdn-uploads.gameblog.fr/images/jeux/0/GameblogNext_02.jpg"

            #response.xpath('//article//figure/).extract()
            item['theme'] = "Jeux Videos"
            yield item

