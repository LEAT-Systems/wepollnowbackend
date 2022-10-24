import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from poll.models import *
from poll.serializers import *

# Create your views here.


@api_view(['GET', 'POST'])
def poll_category(request):
    if request.method == 'GET':
        poll_data = PollCategory.objects.all()
        serialized_data = PollCategorySerializer(poll_data, many=True)
        return Response(serialized_data.data)

    if request.method == 'POST':
        serialized_data = PollCategorySerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

   

@api_view(['GET', 'POST'])
def poll(request):
    if request.method == 'GET':
        poll_category = request.query_params.get('category')
        state_id = request.query_params.get('state')
        if poll_category == 1:
            poll_data = Poll.objects.filter(poll_category = poll_category)
            serialized_data = PollOutputSerializer(poll_data, many=True)
            return Response(serialized_data.data)
        elif poll_category == 2:
            poll_data = Poll.objects.filter(poll_category = poll_category, poll_state = state_id)
            serialized_data = PollOutputSerializer(poll_data, many=True)
            return Response(serialized_data.data)
        poll_data = Poll.objects.filter(poll_category = poll_category, poll_state = state_id)
        serialized_data = PollOutputSerializer(poll_data, many=True)
        return Response(serialized_data.data)
    
    if request.method == 'POST':
        serialized_data = PollInputSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)
