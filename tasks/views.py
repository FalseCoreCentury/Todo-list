from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    View,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.shortcuts import redirect, get_object_or_404, render

from .forms import TaskForm, TagForm
from .models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "website/home.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all().order_by("is_done", "-created_at")


class CompleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = True
        task.save()
        return redirect("tasks:home")


class UndoTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = False
        task.save()
        return redirect("tasks:home")


class TaskDetailView(DetailView):
    model = Task
    template_name = "website/task_detail.html"
    context_object_name = "task"

    def get_queryset(self):
        return Task.objects.all().order_by("is_done", "-created_at")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "website/task_form.html"
    success_url = reverse_lazy("tasks:home")


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = "website/task_form.html"
    context_object_name = "tasks"

    def get_success_url(self):
        return reverse_lazy("tasks:home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "website/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:home")


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("home")


class TagListView(ListView):
    model = Tag
    template_name = "website/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "website/tag_form.html"
    success_url = reverse_lazy("tasks:tags")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "website/tag_confirm_delete.html"
    success_url = reverse_lazy("tasks:tags")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "website/tag_form.html"
    success_url = reverse_lazy("tasks:tags")
