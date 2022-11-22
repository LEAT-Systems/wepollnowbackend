from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from voters.models import Voter
from voters.serializers import VoterSerializer, VoteSerializer
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from utilities.models import State, Lga
from rest_framework import status
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from utilities.pagination import CustomPagination
from poll.models import Votes


    
class Voters(ListCreateAPIView):
    serializer_class = VoterSerializer
    pagination_class = CustomPagination
    queryset = Voter.objects.all()

class Votes(CreateAPIView):
    serializer_class = VoteSerializer
    queryset = Votes.objects.all()

    
       

    
    