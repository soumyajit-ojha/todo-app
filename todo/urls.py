from django.urls import path
from .views import (
    TodoAPIView,
    AllTodoAPIView,
)

urlpatterns = [
    path('todo/', TodoAPIView.as_view(), name='all-todos-list'),
    path('todo/<int:pk>', TodoAPIView.as_view(), name='todo-detail'),
    path('alltodos/', AllTodoAPIView.as_view(), name='all-todo')
]
