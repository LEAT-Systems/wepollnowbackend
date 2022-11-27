from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import BlogSerializer
from .models import Blog


class CreateBlog(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
     
