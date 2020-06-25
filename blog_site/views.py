from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate

from .models import News, Category, User
from .forms import NewsForm, CreationUserForm




def articles(request):
    article=News.objects.filter(is_published=True)

    paginator = Paginator(article, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)



    all_cat=Category.objects.all()
    queryset=News.objects.select_related('Category')
    return render(request, 'blog/article.html', {'news':article, 'all_cat':all_cat, 'page_obj': page_obj})

def category(request, cat_t):
    current_cat=get_object_or_404(Category, title=cat_t)
    all_cat=Category.objects.all()
    selected_news=current_cat.news_set.all()

    paginator = Paginator(selected_news, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    queryset=News.objects.select_related('Category')
    return render(request, 'blog/article.html', {'news':selected_news, 'all_cat':all_cat, 'page_obj': page_obj})

def detailPage(request,news_pk):
    current_art = get_object_or_404(News, pk=news_pk)
    current_art.views = F('views') + 1
    current_art.save()
    current_art.refresh_from_db()
    return render(request, 'blog/detail.html', {'article': current_art})

def registerPage(request):
    form = CreationUserForm()
    if request.method =='POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            User.objects.create(
                user=user, username=request.POST['username'], email=request.POST['email']
            )
            return redirect('login')
    return render(request, 'blog/register.html', {'form':form})

def logoutPage(request):
    logout(request)
    return redirect('mainpage')

def loginPage(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('mainpage')
        
    return render(request, 'blog/login.html')



def createPost(request):
    form = NewsForm()
    if request.method=='POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'blog/createPost.html', {'form': form})
    






