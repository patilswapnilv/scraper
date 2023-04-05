"""
File: middlewares.py
Project: web-scraper

This module contains the middlewares used for the web scraper.

"""

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class JavascriptMiddleware(object):
    """
    Middleware for rendering JavaScript generated content using Selenium
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        super(JavascriptMiddleware, self).__init__()

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def spider_closed(self):
        self.driver.quit()

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(5)
        body = self.driver.page_source
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
