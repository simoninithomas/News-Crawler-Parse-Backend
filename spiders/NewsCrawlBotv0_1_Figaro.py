import scrapy

from NewsCrawlBot.items import FigaroItem

class FigaroSpider(scrapy.Spider):
    name = "Figaro"
    allowed_domains = ["lefigaro.fr"]
    start_urls = [
        "http://www.lefigaro.fr/flash-actu"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="fig-profils"]/section/div'):
            item = FigaroItem()
            item['language'] = "FR"
            item['title'] = sel.xpath('*[self::h1 or self::h2]/a/text()').extract_first(default='')

            if item['title'].startswith('/'):
                item['title'] = "http://www.lefigaro.fr" + item['title']

            item['publisher'] = "Le Figaro"
            item['publishedDate'] = sel.xpath('ul/li[@class="fig-date-maj fig-date-mobile"]/time/@datetime').extract_first(default='')
            item['url'] = 'http://www.lefigaro.fr' + sel.xpath('*[self::h1 or self::h2]/a/@href').extract_first(default='')
            item['image'] = 'http://eedl.eodi.org/wp-content/uploads/sites/3/2016/01/Figaro.png'
            item['theme'] = "Actualites"
            yield item




