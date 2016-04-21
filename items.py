# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.exporter import JsonItemExporter


class MondeItem(scrapy.Item):
     language = scrapy.Field()
     title = scrapy.Field()
     publisher = scrapy.Field()
     publishedDate = scrapy.Field()
     url = scrapy.Field()
     image = scrapy.Field()
     theme = scrapy.Field()


class FigaroItem(scrapy.Item):
     language = scrapy.Field()
     title = scrapy.Field()
     publisher = scrapy.Field()
     publishedDate = scrapy.Field()
     url = scrapy.Field()
     image = scrapy.Field()
     theme = scrapy.Field()

class MaddynessItem(scrapy.Item):
     language = scrapy.Field()
     title = scrapy.Field()
     publisher = scrapy.Field()
     publishedDate = scrapy.Field()
     url = scrapy.Field()
     image = scrapy.Field()
     theme = scrapy.Field()

class S1001StartupsItem(scrapy.Item):
     language = scrapy.Field()
     title = scrapy.Field()
     publisher = scrapy.Field()
     publishedDate = scrapy.Field()
     url = scrapy.Field()
     image = scrapy.Field()
     theme = scrapy.Field()

class ChallengesItem(scrapy.Item):
     language = scrapy.Field()
     title = scrapy.Field()
     publisher = scrapy.Field()
     publishedDate = scrapy.Field()
     url = scrapy.Field()
     image = scrapy.Field()
     theme = scrapy.Field()

class TechCrunchItem(scrapy.Item):
     language = scrapy.Field()
     title = scrapy.Field()
     publisher = scrapy.Field()
     publishedDate = scrapy.Field()
     url = scrapy.Field()
     image = scrapy.Field()
     theme = scrapy.Field()

class FigaroSportItem(scrapy.Item):
     language = scrapy.Field()
     title = scrapy.Field()
     publisher = scrapy.Field()
     publishedDate = scrapy.Field()
     url = scrapy.Field()
     image = scrapy.Field()
     theme = scrapy.Field()


class GorafiItem(scrapy.Item):
     language = scrapy.Field()
     title = scrapy.Field()
     publisher = scrapy.Field()
     publishedDate = scrapy.Field()
     url = scrapy.Field()
     image = scrapy.Field()
     theme = scrapy.Field()

class GameBlogItem(scrapy.Item):
     language = scrapy.Field()
     title = scrapy.Field()
     publisher = scrapy.Field()
     publishedDate = scrapy.Field()
     url = scrapy.Field()
     image = scrapy.Field()
     theme = scrapy.Field()

class EclaireusesItem(scrapy.Item):
     language = scrapy.Field()
     title = scrapy.Field()
     publisher = scrapy.Field()
     publishedDate = scrapy.Field()
     url = scrapy.Field()
     image = scrapy.Field()
     theme = scrapy.Field()

