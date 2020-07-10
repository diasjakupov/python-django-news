from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=100, null=True)
    email=models.EmailField(null=True, blank=True,)
    image=models.ImageField(null=True, blank=True, upload_to='users', default="blank-profile-picture-973460_640.png")

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username, email=instance.email)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



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

    def get_absolute_url(self):
        return reverse('detail', kwargs={'news_pk': self.pk})

class Like(models.Model):
    post=models.ForeignKey(News, null=True, on_delete=models.CASCADE)
    like=models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.like.username







