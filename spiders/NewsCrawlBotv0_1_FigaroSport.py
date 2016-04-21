import scrapy

from NewsCrawlBot.items import FigaroSportItem

class FigaroSportSpider(scrapy.Spider):
    name = "FigaroSport"
    allowed_domains = ["sport24.lefigaro.fr"]
    start_urls = [
        "http://sport24.lefigaro.fr/l-integrale"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="s24-search__results"]//div[@class="s24-card__title"]'):
            item = FigaroSportItem()
            item['language'] = "FR"
            item['title'] = sel.xpath('a/text()').extract_first(default='')
            item['publisher'] = "Le Figaro Sport"
            item['publishedDate'] = 'datetime.utcnow()'
            item['url'] = sel.xpath('//div[@class="s24-card__title"]/a/@href').extract_first(default='')
            if item['url'].startswith('/'):
                item['url'] = "http://sport24.lefigaro.fr" + item['url']
            item['image'] = 'http://apps.site.lefigaro.fr/sites/apps/files/styles/large/public/thumbnails/image/sport24.png?itok=caKsKUzV'
            item['theme'] = "Sport"
            yield item





