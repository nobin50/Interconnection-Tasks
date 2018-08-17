from django.shortcuts import render

from rest_framework import generics

from .models import Contact_List
from .serializers import ContactSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = Contact_List.objects.all()
    serializer_class = ContactSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact_List.objects.all()
    serializer_class = ContactSerializer
