import scrapy

from NewsCrawlBot.items import S1001StartupsItem

class S1001StartupsSpider(scrapy.Spider):
    name = "1001Startups"
    allowed_domains = ["http://1001startups.fr/feed/"]
    start_urls = [
        "http://1001startups.fr/feed/",
    ]

    def parse(self, response):
        for sel in response.xpath('//item'):
            item = S1001StartupsItem()
            item['language'] = "FR"
            item['title'] = sel.xpath('title/text()').extract_first(default='')
            item['publisher'] = "1001 Startups"
            item['publishedDate'] =  sel.xpath('pubDate/text()').extract_first(default='')
            item['url'] = sel.xpath('link/text()').extract_first(default='')
            item['image'] = 'http://1001startups.fr/wp-content/uploads/2016/02/Logo-1001startups-e1454507532484-1.png'
            item['theme'] = "Startups"


            yield item


