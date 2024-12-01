from django.contrib import admin
from .models import Thread, Comment, Category

admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(Category)
# Register your models here.
