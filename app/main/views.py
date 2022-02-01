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
    title = "Flask News API Application"

    search_news=request.args.get('news_query')
    if search_news:
        return redirect(url_for('.search',news_name=search_news))
    else:
        return render_template("index.html",title=title,
                               my_sources=sourcess,my_bbc=bbc_news,
                               google_news=google_news,aljaazera=aljaazera_news)


@main.route('/articles/<source>')
def articles(source):
    """Default function that renders the default page"""
    article=get_articles_news(source)
    title = "Flask News Application"
    return render_template("articles.html",title=title,articles=article)



# Category
@main.route('/general')
def general():
    """method to fetch general data"""
    general_news=articles_category('general')
    sourcess = get_source_news()
    return  render_template('general.html',general=general_news,my_sources=sourcess)

@main.route('/sports')
def Sports():
    """method to fetch sports data"""
    sourcess=get_source_news()

    all_sports=articles_category('sports')
    return render_template("sports.html",sports=all_sports,my_sources=sourcess)


@main.route('/technology')
def technology():
    """method to fetch technology data"""
    technology_news=articles_category('technology')
    sourcess = get_source_news()
    return  render_template('technology.html',technology=technology_news,my_sources=sourcess)



@main.route('/bussiness')
def bussiness():
    """method to fetch bussiness data"""
    sourcess=get_source_news()

    all_bussinesses=articles_category('business')
    return render_template("bussiness.html",bussiness=all_bussinesses,my_sources=sourcess)


@main.route('/entertainment')
def entertainment():
    """method to fetch bussiness data"""
    sourcess=get_source_news()

    entertainment=articles_category('entertainment')
    return render_template("entertainment.html",entertainment=entertainment,my_sources=sourcess)


@main.route('/politics')
def politics():
        """method to fetch politics data"""
        sourcess=get_source_news()

        politics_news=articles_category('politics')
        return render_template('politics.html',politics=politics_news,my_sources=sourcess)


@main.route('/search/<news_name>')
def search(news_name):
    """method to fetch search results"""
    news_name_list = news_name.split(" ")
    search_name_format = "+".join(news_name_list)
    searched_results = search_news(search_name_format)
    sourcess=get_source_news()

    title = f'search results for {news_name}'
    return render_template('search.html', results=searched_results,my_sources=sourcess)