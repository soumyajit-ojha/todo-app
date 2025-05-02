from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Todo
from .serializers import TodoSerializer


    
class TodoListAPIView(APIView):
    """
    A simple API view to for all todos.
    """
    def get(self, request, pk=None, format=None):
        if pk is not None:
            # DETAIL
            todo       = get_object_or_404(Todo, pk=pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=200)

        # LIST
        queryset = Todo.objects.all()
        if not queryset:
            return Response({"message":"No data found"}, status=204)

        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    
class TodoCreateAPIView(APIView):
    """
    APIView to create a new object of todo.
    """
    def post(self, request: Request):
        payload = request.data
        serializer = TodoSerializer(data=payload)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TodoUpdateAPIView(APIView):
    """
    APIView for updating the todo completly.
    """
    def put(self, request: Request, pk: int):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(instance=todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(instance=todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

        
class TodoDeleteAPIView(APIView):
    """
    APIView to delete an existing todo.
    """

    def delete(self, request: Request, pk:int):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return Response({"message" : "No conttent found"}, status=status.HTTP_204_NO_CONTENT)

