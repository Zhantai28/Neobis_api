from django.contrib import admin
from .models import Category, Comment, Product, Cart, Replies

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Comment)
admin.site.register(Replies)
