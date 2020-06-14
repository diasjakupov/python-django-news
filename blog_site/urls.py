from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.articles, name='mainpage'),
    path('<int:cat_pk>', views.category, name='category'),
    path('<str:news_t>', views.detailPage, name='detail'),
]
