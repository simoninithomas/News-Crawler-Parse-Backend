# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import httplib
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log



class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item


class Newscrawlbotv01Pipeline(object):
    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")
        connection = httplib.HTTPSConnection(
            settings['PARSE'],
            settings['PORT']
        )


        connection.connect()
        connection.request('POST', '/1/classes/Articles', json.dumps(dict(item)), {
       "X-Parse-Application-Id": "YOUR PARSE USER ID",
       "X-Parse-REST-API-Key": "YOUR PARSE API KEY",
       "Content-Type": "application/json"
     })
        log.msg("Question added to PARSE !", level=log.DEBUG, spider=spider)
        return item
        #self.collection.update({'url': item['url']}, dict(item), upsert=True)







