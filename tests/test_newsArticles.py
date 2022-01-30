import unittest
from app.news_article import NewsArticles

class NewsSourceTest(unittest.TestCase):
    '''Test Class to test the behaviour of the NewsSource class'''

    def setUp(self):
        '''Set up method that will run before every Test'''
        self.search = NewsArticles('Oliver Haslam','TeslaMic By Tesla Is A Microphone For In-Car Karaoke Sessions','TeslaMic by Tesla is a microphone for in-car karaoke sessions. Here is everything you need to know about this',"https://www.redmondpie.com/teslamic-by-tesla-is-a-microphone-for-in-car-karaoke-sessions/",'"https://cdn.redmondpie.com/wp-content/uploads/2022/01/teslamic.jpg"','2022-01-29T15:15:06Z','Have you ever been sat in your car and wished you could enjoy a good karaoke session')

    def test_instance(self):
        """checks if the object (self.search) is an instance of the NewsSource class."""
        self.assertTrue(isinstance(self.search,NewsArticles))

    # def test_init(self):
    #     """method to check if the object is instantiated correctly """
    #     # author, title, description, url, urlToImage, publishedAt, content

    #     self.assertEqual(self.search.author,'Oliver Haslam')
    #     self.assertEqual(self.search.title, 'TeslaMic By Tesla Is A Microphone For In-Car Karaoke Sessions')
    #     self.assertEqual(self.search.description, 'TeslaMic by Tesla is a microphone for in-car karaoke sessions. Here is everything you need to know about this')
    #     self.assertEqual(self.search.url, "https://www.redmondpie.com/teslamic-by-tesla-is-a-microphone-for-in-car-karaoke-sessions/")
    #     self.assertEqual(self.search.urlToImage, "https://cdn.redmondpie.com/wp-content/uploads/2022/01/teslamic.jpg")
    #     self.assertEqual(self.search.publishedAt, '2022-01-29T15:15:06Z')
    #     self.assertEqual(self.search.content, 'Have you ever been sat in your car and wished you could enjoy a good karaoke session')


