from django.urls import path
from . import views


urlpatterns = [
    path('html/', views.article_html),
    path('json-1/', views.article_json_1),
    path('json-2/', views.article_json_2),
    path('json-3/', views.article_json_3),
    path('articles_list/', views.articles_list),
    path('article_detail/<int:article_pk>/', views.article_detail),
]
