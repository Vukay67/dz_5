from django.urls import path
from .views import main_page, article_page

urlpatterns = [
    path('', main_page, name="main_page"),
    path('article/', article_page, name="article_page")
]
