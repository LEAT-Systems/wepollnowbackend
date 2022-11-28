from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import BlogSerializer
from .models import Blog


class CreateBlog(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
     

class RetrieveOrDeleteBlog(RetrieveDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

