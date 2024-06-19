from django.contrib import admin
from .models import Post, Category, Tag, News, Comment, NewsletterSubscription

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(NewsletterSubscription)