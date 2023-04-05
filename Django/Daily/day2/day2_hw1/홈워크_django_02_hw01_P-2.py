urlpatterns = [
    path('introduce/<str:name>/<int:age>',views.introduce)
]