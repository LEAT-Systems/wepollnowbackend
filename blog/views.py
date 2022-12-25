from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import BlogSerializer
from .models import Blog
from user.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.validators import ValidationError



class CreateBlog(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        try:
            user = self.request.user
            serializer.save(author=user)
            return super().perform_create(serializer)
        except Exception:
            raise ValidationError("Invalid Credentials")
     

class RetrieveOrDeleteBlog(RetrieveDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

