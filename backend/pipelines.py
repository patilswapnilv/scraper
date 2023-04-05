File path: ./scraper/scraper/pipelines.py
import logging
import pymongo

from scrapy.exceptions import DropItem
from scrapy import settings
from scraper.items import ArticleItem

class MongoDBPipeline:
"""
A pipeline to store the scraped data in MongoDB.
"""
def init(self):
"""
Initialize the pipeline.
"""
self.mongo_uri = settings['MONGODB_URI']
self.mongo_db = settings['MONGODB_DB']
self.collection_name = settings['MONGODB_COLLECTION']
self.client = None
self.db = None
self.collection = None

python
Copy code
@classmethod
def from_crawler(cls, crawler):
    """
    Construct the pipeline from the crawler instance.
    """
    pipeline = cls()
    crawler.signals.connect(pipeline.open_spider, signal = 'spider_opened')
    crawler.signals.connect(pipeline.close_spider, signal = 'spider_closed')
    return pipeline

def open_spider(self, spider):
    """
    Open a connection to the MongoDB instance.
    """
    self.client = pymongo.MongoClient(self.mongo_uri)
    self.db = self.client[self.mongo_db]
    self.collection = self.db[self.collection_name]

def close_spider(self, spider):
    """
    Close the connection to the MongoDB instance.
    """
    self.client.close()

def process_item(self, item, spider):
    """
    Process the item and insert into the MongoDB instance.
    """
    if isinstance(item, ArticleItem):
        self.collection.insert_one(dict(item))
        logging.debug("Article added to MongoDB database!")
    else:
        raise DropItem("Item not of valid type, dropping it!")
    return item
class ContentRewriterPipeline:
"""
A pipeline to rewrite the content of scraped articles.
"""
def init(self):
"""
Initialize the pipeline.
"""
self.rewrite_func = None

python
Copy code
@classmethod
def from_crawler(cls, crawler):
    """
    Construct the pipeline from the crawler instance.
    """
    pipeline = cls()
    pipeline.rewrite_func = crawler.settings.get('CONTENT_REWRITE_FUNC')
    return pipeline

def process_item(self, item, spider):
    """
    Process the item and rewrite the content.
    """
    if isinstance(item, ArticleItem) and self.rewrite_func:
        item['content'] = self.rewrite_func(item['content'])
        logging.debug("Article content rewritten!")
    else:
        logging.debug("Skipping content rewrite!")
    return item