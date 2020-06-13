from django.shortcuts import render, HttpResponse
from .models import *


def articles(request):
    article=News.objects.all()
    all_cat=Category.objects.all()
    return render(request, 'blog/article.html', {'news':article, 'all_cat':all_cat})

def category(request, cat_pk):
    current_cat=Category.objects.get(pk=cat_pk)
    all_cat=Category.objects.all()
    selected_news=current_cat.news_set.all()
    return render(request, 'blog/article.html', {'news':selected_news, 'all_cat':all_cat})
    






