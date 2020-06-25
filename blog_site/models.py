from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'




class Category(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'


class News(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField(blank=True)
    image=models.ImageField(upload_to='news', null=True, blank=True)
    is_published=models.BooleanField(default=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    views=models.IntegerField(default=0)
    cat=models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'





