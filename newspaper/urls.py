from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_news, name="home_page_news"),
    path('<int:news_id>/', views.details, name='news_details'),
    
]
