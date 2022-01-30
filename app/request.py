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

# ----------------------------------------Sources----------------------------------

def get_source_news():
    '''Function that gets the json response to our url request'''
    get_news_source_url = 'https://newsapi.org/v2/sources?apiKey={}'.format(api_key)
    news_data_response = requests.get(get_news_source_url).json()
    news_results = None

    if news_data_response['sources']:
        news_results_list = news_data_response['sources']
        news_results = process_results_sources(news_results_list)

    return news_results


def process_results_sources(news_list):
    """Function  that processes the news results and transform them to a list of Objects"""
    news_results = []

    for eachnews in news_list:
        id = eachnews.get('id')
        name = eachnews.get('name')
        description = eachnews.get('description')
        url = eachnews.get('url')
        category = eachnews.get('category')
        language = eachnews.get('language')
        country = eachnews.get('country')

        news_object = NewsSource(id, name, description, url, category, language, country)

        news_results.append(news_object)

    return news_results


# ----------------------------------------Articles----------------------------------

def get_articles_news(source):
    get_news_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(source, api_key)

    news_art = requests.get(get_news_articles_url).json()

    get_news_articles_url = None

    if news_art['articles']:
        news_art_url = news_art['articles']
        get_news_articles_url = process_results_articles(news_art_url)

    return get_news_articles_url


def articles_source(source, pageSize):
    get_articles_by_source = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}&pageSize={}'.format(source,
                                                                                                            api_key,
                                                                                                            pageSize)
    news_articles_source_response = requests.get(get_articles_by_source).json()

    articles_source_results = None

    if news_articles_source_response['articles']:
        news_res = news_articles_source_response['articles']
        articles_source_results = process_results_articles(news_res)

    return articles_source_results

def process_results_articles(news_articles):
    """Function  that processes the news articles results and transform them to a list of Objects"""
    news_articles_process_results = []

    for eachnews in news_articles:
        author = eachnews.get('author')
        title = eachnews.get('title')
        description = eachnews.get('description')
        url = eachnews.get('url')
        urlToImage = eachnews.get('urlToImage')
        publishedAt = eachnews.get('publishedAt')
        content = eachnews.get('content')

        if urlToImage:
            news_object = NewsArticles(author, title, description, url, urlToImage, publishedAt, content)
            news_articles_process_results.append(news_object)

    return news_articles_process_results
