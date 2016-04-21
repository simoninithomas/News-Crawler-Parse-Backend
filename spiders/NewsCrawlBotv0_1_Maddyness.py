import scrapy

from NewsCrawlBot.items import MaddynessItem

class MaddynessSpider(scrapy.Spider):
    name = "Maddyness"
    allowed_domains = ["http://www.maddyness.com/feed/"]
    start_urls = [
        "http://www.maddyness.com/feed/",
    ]

    def parse(self, response):
        image = "http://azertyjobs.com/wp-content/uploads/2013/09/Logo-Maddyness-NOIR-200x200.png"
        for sel in response.xpath('//item'):
            item = MaddynessItem()
            item['language'] = "FR"
            item['title'] = sel.xpath('title/text()').extract_first(default='')
            item['publisher'] = "Maddyness"
            item['publishedDate'] = sel.xpath('pubDate/text()').extract_first(default='')
            item['url'] = sel.xpath('link/text()').extract_first(default='')
            item['image'] = "image"
            item['theme'] = "Startups"
            yield item


