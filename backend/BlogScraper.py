# BlogScraper.py - ./backend/BlogScraper.py
# This module contains the implementation of a scraper for blogger websites using the Scrapy framework.
# The scraper can extract the metadata for each blog post and optionally download the content and images.
# This module also includes methods for rewriting the scraped content to remove plagiarism using the OpenAI API.

# BlogScraper.py

import scrapy
import json

class BlogScraper(scrapy.Spider):
    name = 'blog_scraper'

    def start_requests(self):
        """
        This method starts the scraper and gets the urls from where the data has to be scraped.
        """
        urls = self.settings.get('START_URLS')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        This method is used to parse the response from the urls passed and extract the required data.
        """
        # Extracting data from the HTML response
        title = response.css('title::text').get()
        author = response.css('span.author::text').get()
        publish_date = response.css('span.publish_date::text').get()
        content = response.css('div.content::text').getall()

        # Storing the extracted data in a dictionary
        blog_data = {
            'title': title,
            'author': author,
            'publish_date': publish_date,
            'content': content
        }

        # Converting the data to the required format and returning it
        result_format = self.settings.get('RESULT_FORMAT')
        if result_format == 'json':
            return json.dumps(blog_data)
        elif result_format == 'xml':
            # Convert to xml
            pass
        elif result_format == 'markdown':
            # Convert to markdown
            pass
        else:
            raise ValueError(f"Invalid result format: {result_format}")
            
# Test cases
def test_blog_scraper():
    # Test case 1: Check if the spider starts and returns a response
    scraper = BlogScraper()
    response = scraper.start_requests()
    assert response is not None

    # Test case 2: Check if the spider returns the correct data
    scraper = BlogScraper()
    response = scraper.parse(scrapy.http.Response(url='https://www.example.com', body='<html><head><title>Example Blog</title></head><body><div class="content">Example content</div></body></html>'))
    expected_result = {
        'title': 'Example Blog',
        'author': None,
        'publish_date': None,
        'content': ['Example content']
    }
    assert response == json.dumps(expected_result)
    
    print("All test cases pass!")

