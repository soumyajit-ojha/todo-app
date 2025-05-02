from django.urls import path
from .views import TodoAPIView

urlpatterns = [
    path('todo/', TodoAPIView.as_view(), name='all-todos-list'),
    path('todo/<int:pk>', TodoAPIView.as_view(), name='todo-detail'),
]
