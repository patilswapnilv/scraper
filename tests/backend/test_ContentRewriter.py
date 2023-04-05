import unittest
from content.ContentRewriter import ContentRewriter

class TestContentRewriter(unittest.TestCase):

    def test_rewriter(self):
        # create an instance of the ContentRewriter
        rewriter = ContentRewriter()

        # define some dummy text
        dummy_text = "This is a dummy text. It has a sentence with the word 'Python' in it."

        # apply the rewrite method
        rewritten_text = rewriter.rewrite(dummy_text)

        # check if the word 'Python' has been replaced with 'JavaScript'
        self.assertNotIn('Python', rewritten_text)
        self.assertIn('JavaScript', rewritten_text)

if __name__ == '__main__':
    unittest.main()
