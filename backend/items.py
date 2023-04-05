# items.py
# Defines the data structure for the scraped items

import scrapy

class BlogscraperItem(scrapy.Item):
    # Define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    publish_date = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    images = scrapy.Field()
