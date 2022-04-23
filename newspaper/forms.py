from pyexpat import model
from .models import Newspaper
from django import forms


class CreatFormItem(forms.ModelForm):
    class Meta:
          model =  Newspaper
          fields = ["news_title", "news_decription", "news_video", "news_audio", "news_image", "news_author"] 
    