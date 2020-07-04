from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.decorators.cache import cache_page

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages

from .models import News, Category, User
from .forms import NewsForm, CreationUserForm

from django.core.mail import send_mail
from django.contrib.auth.models import User as request_user
import random


    


def mail(request):
    global num
    num=str(random.randint(0, 10000))
    send_mail('Subject here', num, 'dias.dzhakupov.68@mail.ru',
    [person.email], fail_silently=False)

# @cache_page(60*2)
def articles(request):
    article=News.objects.filter(is_published=True)    

    paginator = Paginator(article, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    queryset=News.objects.select_related('Category')


    return render(request, 'blog/article.html', {'news':article, 'page_obj': page_obj})

def category(request, cat_t):
    current_cat=get_object_or_404(Category, title=cat_t)
    all_cat=Category.objects.all()
    selected_news=current_cat.news_set.filter(is_published=True)

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
            messages.success(request, 'Аккаунт создан')
            return redirect('login')
    return render(request, 'blog/register.html', {'form':form})

def logoutPage(request):
    logout(request)
    return redirect('mainpage')

def loginPage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mainpage') 
        else:
            messages.error(request, 'Ошибка входа')       
    return render(request, 'blog/login.html')



def createPost(request):
    form = NewsForm()
    if request.method=='POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'blog/createPost.html', {'form': form})

def forget_pass(request):
    if request.method=='POST':
        email=request.POST['email']
        global person
        person=request_user.objects.get(email=email)
        mail(request)
        return redirect('change')
        
    return render(request, 'blog/create_password1.html')

def password_change(request):
    if request.method=='POST':
        if request.POST['number']==num:
                person.set_password(request.POST['password'])            
                person.save()
                messages.success(request, 'Пароль успешно изменен')
                return redirect('login')
    return render(request, 'blog/create_password2.html')


@login_required(login_url='login')
def like(request, article_pk):
    art=News.objects.get(pk=article_pk)
    list_user_id=[]
    if art.like_set.all():
        print('1')
        for i in art.like_set.all():
            list_user_id.append(i.like.id)
        if request.user.user.id in list_user_id:
            print(list_user_id)             
            print('ok')
            art.like_set.get(like=request.user.user.pk).delete()
            print('delete')
        else:
            print(list_user_id)
            print('create')
            art.like_set.create(like=request.user.user, post=art)
    else:
        print('create')
        art.like_set.create(like=request.user.user, post=art)
            
    return redirect(art)

def profile(request):
    return render(request, 'blog/profile.html')
    
    

    






