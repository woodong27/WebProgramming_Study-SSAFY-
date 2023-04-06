from django.contrib import admin
from .models import Movie

# Register your models here.
class List(admin.ModelAdmin):
    list_display=('pk','title','genre','director')

admin.site.register(Movie, List)
