from flask import render_template,request,url_for,redirect
from . import main
from ..request import get_source_news,articles_source,get_articles_news,articles_category,search_news
# Definition of all views

@main.route('/')
def index():
    """Default function that renders the default page"""
    sourcess=get_source_news()
    bbc_news = articles_source('bbc-news', '8')
    aljaazera_news= articles_source('al-jazeera-english', '8')
    google_news = articles_source('google-news',8)
    title = "Flask News Application"

    search_news=request.args.get('news_query')
    if search_news:
        return redirect(url_for('.search',news_name=search_news))
    else:
        return render_template("index.html",title=title,
                               my_sources=sourcess,my_bbc=bbc_news,
                               google_news=google_news,aljaazera=aljaazera_news)

