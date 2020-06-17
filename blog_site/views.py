from django.shortcuts import render, HttpResponse
from .models import News, Category
from django.shortcuts import get_object_or_404
from django.db.models import F
from .forms import NewsForm


def articles(request):
    article=News.objects.all()
    all_cat=Category.objects.all()
    queryset=News.objects.select_related('Category')
    return render(request, 'blog/article.html', {'news':article, 'all_cat':all_cat})

def category(request, cat_t):
    current_cat=get_object_or_404(Category, title=cat_t)
    all_cat=Category.objects.all()
    selected_news=current_cat.news_set.all()
    queryset=News.objects.select_related('Category')
    return render(request, 'blog/article.html', {'news':selected_news, 'all_cat':all_cat})

def detailPage(request,news_pk):
    current_art = get_object_or_404(News, pk=news_pk)
    current_art.views = F('views') + 1
    current_art.save()
    current_art.refresh_from_db()
    return render(request, 'blog/detail.html', {'article': current_art})

def createPost(request):
    form = NewsForm()
    return render(request, 'blog/createPost.html', {'form': form})
    






