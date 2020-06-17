from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.articles, name='mainpage'),
    path('<str:cat_t>', views.category, name='category'),
    path('news/<int:news_pk>', views.detailPage, name='detail'),
    path('/createPost', views.createPost, name='createPost')
]
