# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from collections import OrderedDict
import pymongo
from jrjmarket.settings import MONGO_CLIENT,MONGO_DB,MONGO_COLLECTION


class JrjmarketPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_CLIENT, 27017)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]

    def process_item(self, item, spider):
        try:
            item['Employee_Count']=int(item['Employee_Count'])
        except:
            pass

        self.collection.insert(OrderedDict(item))

        return item
