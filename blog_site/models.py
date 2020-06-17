from django.db import models


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
    image=models.ImageField(blank=True, upload_to='news', default='news/maxresdefault.jpg')
    is_published=models.BooleanField(default=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    views=models.IntegerField(default=0)
    cat=models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'





