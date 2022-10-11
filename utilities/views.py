from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utilities.models import Lga, States
from utilities.serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def states(request):
    if request.method == 'GET':
        state_data = States.objects.all()
        serialized_data = StateSerializer(state_data, many=True)
        return Response(serialized_data.data)

    if request.method == 'POST': 
        serialized_data = StateSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)
    

@api_view(['GET', 'PUT', 'DELETE'])
def states_by_id(request, pk):
    state_data = States.objects.get(pk=pk)
    if request.method == 'GET':
        serialized_data = StateSerializer(state_data)
        return Response(serialized_data.data)

    if request.method == 'PUT':
        serialized_data = StateSerializer(state_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)

    if request.method == 'DELETE':
        state_data.delete() 
        return Response()

#LGA APIs

@api_view(['GET','POST'])
def lga(request):
        if request.method == 'GET':
            lga_data = Lga.objects.all()
            serialized_data = LgaSerializer(lga_data, many=True)
            return Response(serialized_data.data)

        if request.method == 'POST': 
            serialized_data = LgaSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data)
            else:
                return Response(serialized_data.errors)

@api_view(['GET'])
def lga_by_state(request, state_id):
    if request.method == 'GET':
        data = Lga.objects.all().filter(state_id = state_id)
        serialized_data = LgaSerializer(data, many='True')
        return Response(serialized_data.data)

@api_view(['GET'])
def lga_by_senatorial(request, senatorial_id):
    if request.method == 'GET':
        data = Lga.objects.all().filter(senatorial_id = senatorial_id)
        serialized_data = LgaSerializer(data, many='True')
        return Response(serialized_data.data)

@api_view(['GET', 'POST'])
def senatorial(request):
    if request.method == 'POST':
        serialized_data = SenatorialSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

    if request.method == 'GET':
        senatorial_data = Senatorial.objects.all()
        serialized_data = StateSerializer(senatorial_data, many=True)
        return Response(serialized_data.data)

@api_view(['GET', 'UPDATE', 'DELETE'])
def senatorial_by_state(request, state_id):
    if request.method == 'GET':
        data = Senatorial.objects.all().filter(state_id = state_id)
        serialized_data = SenatorialSerializer(data, many='True')
        return Response(serialized_data.data)