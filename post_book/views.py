from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

class PostBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RetrieveBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer