from typing import Any
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Todo
from django.urls import reverse, reverse_lazy
from .forms import TodoForm, MessageForm
from django.contrib.messages.views import SuccessMessageMixin


class TodoList2(ListView, UpdateView):
    model = Todo
    form_class = TodoForm
    context_object_name = "todoItems"
    template_name = "TodoApp/todo_list.html"
    success_url = reverse_lazy("TodoApp:list")


class TodoList(ListView):
    model = Todo
    fields = "__all__"
    context_object_name = "todoItems"


class TodoDetail(DetailView):
    model = Todo
    context_object_name = "todoItem"


class TodoCreate(SuccessMessageMixin, CreateView):
    model = Todo
    # fields = "__all__"
    form_class = TodoForm
    template_name = "TodoApp/todo_update.html"
    success_message = "新規登録を行いました。"

    # success_url = reverse_lazy("TodoApp:list")
    def get_success_url(self):
        return reverse("TodoApp:create")


class TodoUpdate(SuccessMessageMixin, UpdateView):
    model = Todo
    # fields = "__all__"
    form_class = TodoForm
    template_name = "TodoApp/todo_update.html"
    success_message = "更新しました。"
    # success_url = reverse_lazy("TodoApp:list")

    def get_success_url(self):
        return reverse("TodoApp:update", kwargs={"pk": self.kwargs["pk"]})


class TodoDelete(DeleteView):
    model = Todo
    fields = "__all__"
    template_name = "TodoApp/todo_delete.html"
    success_url = reverse_lazy("TodoApp:list")


class TodoForm(FormView):
    template_name = "TodoApp/todo_form.html"
    form_class = MessageForm
    success_url = reverse_lazy("TodoApp:form")

    def form_valid(self, form):
        introduction = (
            f"{form.cleaned_data['msgTo']}宛てに「{form.cleaned_data['msgTo']}」と送付しておきます。"
        )
        # context = {'form': form, 'intro': introduction}
        context = {"form": form, "message": introduction}
        return render(self.request, self.template_name, context)
