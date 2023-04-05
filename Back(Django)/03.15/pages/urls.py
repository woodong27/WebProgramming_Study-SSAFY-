from django.urls import path
from . import views

app_name='pages'
urlpatterns=[
    path('app1/', views.app1, name='app1')
]