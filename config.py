import os

class Config:
    # NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'

    """main class for both production and development stages"""
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    BASE_SOURCE='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}&pageSize={}'
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_ART_BASE='https://newsapi.org/v2/top-headlines?category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    """class that defines methods and properties to be used on production stage"""
    pass


class DevConfig(Config):
    """class that defines methods and properties to be used on production stage"""
    DEBUG = True


# For accessing different configuration option classes
config_options={
    'development':DevConfig,
    'production':ProdConfig
}