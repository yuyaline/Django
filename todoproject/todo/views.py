from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from .models import TodoModel
from django.urls import reverse_lazy

class TodoList(ListView):
    template_name = "list.html"
    model = TodoModel

class TodoDetail(DetailView):
    template_name = "detail.html"
    model = TodoModel

class TodoCreate(CreateView):
    template_name = "create.html"
    model = TodoModel
    # フォームに表示するフィールドを指定する
    fields = ("title","memo","priority","duedate")
    success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
    template_name = "delete.html"
    model = TodoModel
    success_url = reverse_lazy("list")

class TodoUpdate(UpdateView):
    template_name = "update.html"
    model = TodoModel
    fields = ("title","memo","priority","duedate")
    success_url = reverse_lazy("list")
