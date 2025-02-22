from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display=('id','title','views', 'pub_date', 'is_published')
    list_display_links=('id','title',)
    list_editable=('is_published',)
    readonly_fields=('views',)





admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Profile)

