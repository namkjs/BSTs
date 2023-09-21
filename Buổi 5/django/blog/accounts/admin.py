from django.contrib import admin
from .models import Blogs , BlogCategory
from .models import Item

# Register your models here.

admin.site.register(Blogs)
admin.site.register(BlogCategory)
admin.site.register(Item)