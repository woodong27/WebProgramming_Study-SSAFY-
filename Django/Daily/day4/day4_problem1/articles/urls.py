from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
]
