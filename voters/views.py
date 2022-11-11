from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from voters.models import Voter
from voters.serializers import VoterSerializer
from rest_framework.generics import ListCreateAPIView
from utilities.models import State, Lga
    
class Voters(ListCreateAPIView):
    serializer_class = VoterSerializer
    queryset = Voter.objects.all()
    
    