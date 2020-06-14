from django.shortcuts import render, HttpResponse
from .models import News, Category
from django.shortcuts import get_object_or_404


def articles(request):
    article=News.objects.all()
    all_cat=Category.objects.all()
    return render(request, 'blog/article.html', {'news':article, 'all_cat':all_cat})

def category(request, cat_pk):
    current_cat=Category.objects.get(pk=cat_pk)
    all_cat=Category.objects.all()
    selected_news=current_cat.news_set.all()
    return render(request, 'blog/article.html', {'news':selected_news, 'all_cat':all_cat})

def detailPage(request, news_t):
    current_art = get_object_or_404(News, title=news_t)
    current_art.views=current_art.views + 1
    current_art.save()
    return render(request, 'blog/detail.html', {'article': current_art})
    






