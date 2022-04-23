from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_news, name="home_page_news"),
    path('<int:news_id>/', views.details, name='news_details'),
    # path('update/<int:id>/', views.update_news_field, name="update_news"),
    path("creat_news/", views.creat_news, name="creat_news_item"),
    
]
