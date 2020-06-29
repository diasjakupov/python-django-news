from django import template
from django.db.models import Count
from blog_site.models import *

register = template.Library()

@register.inclusion_tag('blog/sidebar.html')
def get_news_count():
    cat=Category.objects.filter(news__is_published=True).annotate(cnt=Count('news'))
    return {'cat': cat}