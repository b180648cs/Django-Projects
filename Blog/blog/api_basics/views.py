from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .serializers import ToDoSerializer


class  ToDoList(APIView):
    def get(self,request):
        ToDo1=ToDo.objects.all()
        serializer=ToDoSerializer(ToDo1,many=True)
        return Response({"ToDo": serializer.data})

    def post(self, request):


        # Create an article from the above data
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class ToDoDetail(APIView):
    def get_object(self, id):
        try:
            return ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = ToDoSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = ToDoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer=ToDo(snippet);
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









# Create your views here.
