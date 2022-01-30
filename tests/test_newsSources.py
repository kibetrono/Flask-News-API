import unittest
from app.news_source import NewsSource


class NewsSourceTest(unittest.TestCase):
    '''Test Class to test the behaviour of the NewsSource class'''

    def setUp(self):
        '''Set up method that will run before every Test'''
        self.search = NewsSource(1,'Flask Application','A developing Python Framework','https://pypi.org/project/Flask/','technology','en','kenya')

    def test_instance(self):
        """checks if the object (self.search) is an instance of the NewsSource class."""
        self.assertTrue(isinstance(self.search,NewsSource))

    def test_init(self):
        """method to check if the object is instantiated correctly"""

        self.assertEqual(self.search.id,1)
        self.assertEqual(self.search.name, 'Flask Application')
        self.assertEqual(self.search.description, 'A developing Python Framework')
        self.assertEqual(self.search.url, 'https://pypi.org/project/Flask/')
        self.assertEqual(self.search.category, 'technology')
        self.assertEqual(self.search.language, 'en')
        self.assertEqual(self.search.country, 'kenya')


