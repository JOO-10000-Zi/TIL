from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(Article)
admin.site.register(Comment)