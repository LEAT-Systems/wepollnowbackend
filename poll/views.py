import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from poll.models import *
from poll.serializers import *

# Create your views here.


@api_view(['POST', 'GET'])
def add_poll_category(request):
    if request.method == 'POST':
        serialized_data = PollCategorySerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

    if request.method == 'GET':
        poll_data = PollCategory.objects.all()
        serialized_data = PollCategorySerializer(poll_data, many=True)
        return Response(serialized_data.data)
