from django.urls import path
from . import views

app_name='articles'
urlpatterns=[
    path('app1/', views.app1, name='app1'),
    path('app2/', views.app2, name='app2')
]