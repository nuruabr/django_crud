from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_news, name="home_page_news"),
    
]
