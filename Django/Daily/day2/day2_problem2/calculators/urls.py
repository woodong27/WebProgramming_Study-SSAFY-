from django.urls import path
from . import views

app_name='calculators'
urlpatterns=[
    path('calculator/<int:first>/<int:second>', views.calculator, name='calculator'),
]