from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Todo
from .serializers import TodoSerializer


    
class TodoAPIView(APIView):
    """
    A simple API view to for all todos and any specific todo.
    Depending upon path parameter. If no parameter return all todos, 
    if any specif id return specific todo.
    """

    def get(self, request, pk=None, format=None):
        if pk is not None:
            todo       = get_object_or_404(Todo, pk=pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)

        queryset = Todo.objects.all()
        if not queryset:
            return Response({"message":"No data found"}, status=status.HTTP_204_NO_CONTENT)

        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        """
        APIView post method to create a new object of todo.
        """
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request: Request, pk: int):
        """
        APIView patch method to fully update a todo object.
        """
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(instance=todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int):
        """
        APIView patch method to partialy update a todo object.
        """
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(instance=todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

       
    def delete(self, request: Request, pk:int):
        """
        APIView delete method to delete a todo object.
        """
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()

        return Response({"message" : "No conttent found"}, status=status.HTTP_204_NO_CONTENT)

