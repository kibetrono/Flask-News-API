import requests

from .news_article import NewsArticles
from .news_source import NewsSource

# Getting api key
api_key = None

# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key, base_url, base_source, articles_url, category_url
    api_key = app.config['NEWS_API_KEY']
    # base_url = app.config['News_API_Base_URL']
    base_source = app.config['BASE_SOURCE']
    articles_url = app.config['NEWS_API_ARTICLES_URL']
    category_url = app.config['NEWS_ART_BASE']

