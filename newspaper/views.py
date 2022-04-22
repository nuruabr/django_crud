from django.shortcuts import render

# Create your views here.

def home_page_news(request):
    context = {
        'hello': "THIS IS HOME PAGE",
    }
    return render(request, 'newspaper/home.html', context)