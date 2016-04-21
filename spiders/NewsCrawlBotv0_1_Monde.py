import scrapy

from NewsCrawlBot.items import MondeItem

class MondeSpider(scrapy.Spider):
    name = "Monde"
    allowed_domains = ["lemonde.fr"]
    start_urls = [
        "http://www.lemonde.fr/actualite-en-continu/",
    ]

    def parse(self, response):
        for sel in response.xpath('//article'):
            item = MondeItem()
            item['language'] = "FR"
            item['title'] = sel.xpath('div/div/h3/a/text()').extract_first(default='')
            item['publisher'] = "Le Monde"
            item['publishedDate'] =  sel.xpath('time/@datetime').extract_first(default='')
            item['url'] = 'http://www.lemonde.fr' + sel.xpath('//article//a/@href').extract_first(default='')
            item['image'] = 'http://toutelaculture.com/wp-content/uploads/2014/12/logo-le-monde.jpg' #sel.xpath('//img/@data-hd-src').extract_first(default='')
            item['theme'] = "Actualites"
            yield item

