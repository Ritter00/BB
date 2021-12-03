from django.contrib import admin

# Register your models here.
from .models import Poster, ResponseTTPoster, Category


admin.site.register(Poster)
admin.site.register(ResponseTTPoster)
admin.site.register(Category)