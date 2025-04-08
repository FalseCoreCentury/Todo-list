from django.urls import path
from .views import (
    TaskListView,
    ToggleTaskStatusView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    complete_task,
    undo_task,
    TagListView,
    TagCreateView,
    TaskUpdateView,
    TagDeleteView,
    TagUpdateView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("toggle/<int:pk>/", ToggleTaskStatusView.as_view(), name="toggle_status"),
    path("task/<int:pk>/complete/", complete_task, name="task_complete"),
    path("task/<int:pk>/undo/", undo_task, name="undo_task"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
]

app_name = "tasks"
