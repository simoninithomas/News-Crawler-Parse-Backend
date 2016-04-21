import scrapy

from NewsCrawlBot.items import TechCrunchItem

class S1001StartupsSpider(scrapy.Spider):
    name = "TechCrunch"
    allowed_domains = ["http://techcrunch.com/"]
    start_urls = [
        "http://techcrunch.com/",
    ]


    def parse(self, response):
        for sel in response.xpath('//ul[@id="river1"]/li//h2'):
            item = TechCrunchItem()
            item['language'] = "EN"
            item['title'] = sel.xpath('a/text()').extract_first(default='')
            item['publisher'] = "TechCrunch"
            item['publishedDate'] = sel.xpath('//time/@datetime').extract_first(default='')
            item['url'] =  sel.xpath('a/@href').extract_first(default='')
            item['image'] = 'https://tctechcrunch2011.files.wordpress.com/2014/04/tc-logo.jpg'#sel.xpath('//a/img/@data-src').extract_first(default='')
            item['theme'] = "Technologie"
            yield item






    '''def parse(self, response):
        for sel in response.xpath('//ul[@id="river1"]/li//h2'):
            item = TechCrunchItem()
            item['language'] = "EN"
            item['title'] = sel.xpath('a/text()').extract_first(default='')
            item['publisher'] = "TechCrunch"
            item['publishedDate'] = sel.xpath('//time/@datetime').extract_first(default='')
            item['url'] =  sel.xpath('//h2[@class="post-title"]/a/@href').extract_first(default='')
        for sel in response.xpath('//ul[@id="river1"]/li/div/div/span/a'):
            item['image'] = sel.xpath('img/@data-src').extract_first(default='')
            item['theme'] = "Technologie"
            yield item


def parse(self, response):
        for sel in response.xpath('//ul[@id="river1"]/li//div[@class="block block-thumb"]'):
            item = TechCrunchItem()
            item['language'] = "EN"
            item['title'] = sel.xpath('//h2[@class="post-title"]/a/text()').extract_first(default='')
            item['publisher'] = "TechCrunch"
            item['publishedDate'] = sel.xpath('//time/@datetime').extract_first(default='')
            item['url'] =  sel.xpath('//h2[@class="post-title"]/a/@href').extract_first(default='')
            item['image'] = sel.xpath('//a/img/@data-src').extract_first(default='')
            item['theme'] = "Technologie"
            yield item'''


