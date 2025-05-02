from django.urls import path
from .views import (
    TodoCreateAPIView,
    TodoListAPIView,
    TodoUpdateAPIView,
    TodoDeleteAPIView,
    # TodoPartialUpdateAPIVIew
)

urlpatterns = [
    path('todos/', TodoListAPIView.as_view(), name='all-todos'),
    path('todo/<int:pk>', TodoListAPIView.as_view(), name='view-todo'),
    path('todo/create/', TodoCreateAPIView.as_view(), name='create-todo'),
    path('todo/update/<int:pk>', TodoUpdateAPIView.as_view(), name='update-todo'),
    # path('todo/part_update/<int:pk>', TodoPartialUpdateAPIVIew.as_view(), name='part-update-todo'),
    path('todo/delete/<int:pk>', TodoDeleteAPIView.as_view(), name='delete-todo'),
]
