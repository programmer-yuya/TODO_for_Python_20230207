from django.urls import path
from . import views

app_name = 'TestApp3'
urlpatterns = [
    path('', views.index, name='index'),
]