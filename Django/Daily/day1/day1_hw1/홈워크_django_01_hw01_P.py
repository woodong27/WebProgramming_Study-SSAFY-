from django.urls import path
from articles import views

urlpatterns = [
    path('hello', views.hello)
]