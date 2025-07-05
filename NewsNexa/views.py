from django.shortcuts import render
from news_api.api import api_fetching
def home(request):
    api=api_fetching()
    news_data=api.fetch_news()  
    results=news_data['results']
    nextPage=news_data['nextPage']
    if request.method=="POST":
        query=request.POST.get("query")
        query_data=api.fetch_news_by_keyword(query)
        query_results=query_data['results']
        query_data_next_page=query_data['nextPage']
        sent_query_data={
            "query_results":query_results,
            "query_data_next_page":query_data_next_page
        }
        return render(request,"keyword.html",sent_query_data)
    categories = [
    'business',
    'crime',
    'domestic',
    'education',
    'entertainment',
    'environment',
    'food',
    'health',
    'lifestyle',
    'politics',
    'science',
    'sports',
    'technology',
    'top',
    'tourism',
    'world',
    'other'
   ]

    sent_data={
        'results':results,
        'nextPage':nextPage,
        'categories':categories
        }
    return render(request,"home.html",sent_data)

def category(request,category):
    api=api_fetching()
    news_data=api.fetch_news_by_category(category=category)
    cat=category
    results=news_data['results']
    nextPage=news_data['nextPage']
    sent_data={
        'results':results,
        'nextPage':nextPage,
        'category':cat
        }
    return render(request,"category.html",sent_data)
