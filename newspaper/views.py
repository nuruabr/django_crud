from django.shortcuts import render
from .models import Newspaper
# Create your views here.

def home_page_news(request):
    news = Newspaper.objects.all()
    
    context = {
        'news': news,
    }
    return render(request, 'newspaper/home.html', context)


def details(request, news_id):
     details_news = Newspaper.objects.get(pk=news_id)
     context = {
         'details_news': details_news,
     }
     return render(request, 'newspaper/detail.html', context)