from django.urls import path
from .views import (
    TaskListView,
    ToggleTaskStatusView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TaskUpdateView,
    TagDeleteView,
    TagUpdateView,
    CompleteTaskView,
    UndoTaskView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/toggle", ToggleTaskStatusView.as_view(), name="toggle_status"),
    path("task/<int:pk>/complete/", CompleteTaskView.as_view(), name="task_complete"),
    path("task/<int:pk>/undo/", UndoTaskView.as_view(), name="undo_task"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
]

app_name = "tasks"
