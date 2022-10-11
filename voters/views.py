from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from voters.models import Voter
from voters.serializers import VoterSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def voters(request):
    if request.method == 'GET':
        data = Voter.objects.all()
        serialized_data = VoterSerializer(data, many=True)
        return Response(serialized_data.data)
    if request.method == 'POST':
        serialized_data = VoterSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def voter_by_id(request, pk):
    if request.method == 'GET':
        data = Voter.objects.get(pk = pk)
        serialized_data = VoterSerializer(data)
        return Response(serialized_data.data)