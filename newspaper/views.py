from urllib import request
from django.shortcuts import redirect, render
from .models import Newspaper
from .forms import CreatFormItem
# Create your views here.    
"""def update_news_field(request, id):
      update = Newspaper.objects.get(id=id)"""
     

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
 
def creat_news(request):
    form = CreatFormItem(request.POST or None)
     
    if form.is_valid():
        form.save()
        return redirect('home_page_news')
 
    return render(request, "newspaper/creat_item.html", {"form": form})


def update_news(request, id):
    update_news_item =Newspaper.objects.get(id=id)
    form = CreatFormItem(request.POST or None, instance=update_news_item)
    
    if form.is_valid():
        form.save()
        return redirect('home_page_news')
 
    return render(request, 'newspaper/creat_item.html', {"form": form, "update_news_item":update_news_item})
 
