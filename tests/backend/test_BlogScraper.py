import unittest
from unittest.mock import patch, MagicMock

from scraper.backend.BlogScraper import BlogScraper


class TestBlogScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = BlogScraper()

    @patch('scraper.backend.BlogScraper.requests.get')
    def test_get_page(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'<html><body></body></html>'
        mock_requests.return_value = mock_response

        url = 'https://www.example.com'
        response = self.scraper.get_page(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, mock_response.content)

    @patch('scraper.backend.BlogScraper.requests.get')
    def test_get_page_failed_request(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_requests.return_value = mock_response

        url = 'https://www.example.com'
        response = self.scraper.get_page(url)

        self.assertEqual(response.status_code, 404)
        self.assertIsNone(response.content)

    def test_parse_page(self):
        html = '''
            <html>
                <head></head>
                <body>
                    <div class="post">
                        <h2>Post 1</h2>
                        <p>This is the first post</p>
                    </div>
                    <div class="post">
                        <h2>Post 2</h2>
                        <p>This is the second post</p>
                    </div>
                </body>
            </html>
        '''

        expected = [
            {'title': 'Post 1', 'content': 'This is the first post'},
            {'title': 'Post 2', 'content': 'This is the second post'}
        ]

        parsed = self.scraper.parse_page(html)

        self.assertEqual(parsed, expected)

if __name__ == '__main__':
    unittest.main()
