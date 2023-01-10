from django.contrib import admin

from blog.models import Blog, Category, Image

admin.site.register(Blog)
admin.site.register(Image)
admin.site.register(Category)

