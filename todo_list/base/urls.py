from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, SignUpView

urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
]
