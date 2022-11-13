from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from voters.models import Voter
from voters.serializers import VoterSerializer
from rest_framework.generics import ListCreateAPIView
from utilities.models import State, Lga
from rest_framework import status
from django.http import Http404

    
class Voters(ListCreateAPIView):
    serializer_class = VoterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_create(serializer)    
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        voters= Voter.objects.all()
        serializer = self.serializer_class(instance=voters, many = True)
        try:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":"invalid request"}, status=status.HTTP_400_BAD_REQUEST)
       

    
    