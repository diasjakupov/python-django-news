from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.articles, name='mainpage'),
    path('category/<str:cat_t>', views.category, name='category'),
    path('news/<int:news_pk>', views.detailPage, name='detail'),
    path('createPost', views.createPost, name='createPost'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('google_logout', views.logoutPage, name='logout'),
    path('forget_password', views.forget_pass, name='forget'),
    path('change_password', views.password_change, name='change'),
    path('like/<int:article_pk>', views.like, name='like'),
    path('profile', views.profile, name='profile')

]
