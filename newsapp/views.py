from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def Index(request):
    newsapi = NewsApiClient(api_key='9b550a14eabc44f492a080cd1d101027')
    topheadlines = newsapi.get_top_headlines(sources='the-times-of-india')

    articles = topheadlines['articles']
    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    my_list= zip(news, desc, img)


    return render(request, 'index.html', {'mylist':my_list})
