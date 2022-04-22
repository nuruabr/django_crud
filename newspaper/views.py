from django.shortcuts import render
from .models import Newspaper
# Create your views here.

def home_page_news(request):
    news = Newspaper.objects.all()
    
    context = {
        'news': news,
    }
    return render(request, 'newspaper/home.html', context)