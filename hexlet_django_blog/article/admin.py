from django.contrib import admin
from .models import Article
from django.contrib.admin import DateFieldListFilter

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'body']
    list_display = ('name', 'created_at')
    list_filter = (('created_at', DateFieldListFilter),)