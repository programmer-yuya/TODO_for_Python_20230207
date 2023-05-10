from django.urls import path
from . import views
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete, TodoForm
from .views import TemplateView

# from .views import TodoList,CreateView,DetailView,UpdateView,ListView
from django.contrib import admin

app_name = "TodoApp"

urlpatterns = [
    path("", TodoList.as_view(), name="list"),
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
    path("create/", TodoCreate.as_view(), name="create"),
    path("update/<int:pk>", TodoUpdate.as_view(), name="update"),
    path("delete/<int:pk>", TodoDelete.as_view(), name="delete"),
    path("form", TodoForm.as_view(), name="form")
    # path("",TemplateView.as_view(template_name="TodoApp/index.html"),name="index"),
    # path("", views.index),
]
