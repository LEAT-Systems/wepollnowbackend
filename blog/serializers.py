from .models import Blog
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.CharField(required=False)
    

    class Meta:
        model = Blog
        fields = "__all__"


