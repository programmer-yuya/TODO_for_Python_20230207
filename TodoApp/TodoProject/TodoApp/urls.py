from django.urls import path
from . import views

app_name = 'TodoApp'
urlpatterns = [
    path('', views.index, name='index'),
]