from django.contrib import admin
from .models import Article , Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'body',
        'author',
        'date',
    ]
class CommentLine(admin.StackedInline):
    model = Comment
    extra = 0


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)