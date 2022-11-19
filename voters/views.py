from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from voters.models import Voter
from voters.serializers import VoterSerializer
from rest_framework.generics import ListCreateAPIView
from utilities.models import State, Lga
from rest_framework import status
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from utilities.pagination import CustomPagination


    
class Voters(ListCreateAPIView):
    serializer_class = VoterSerializer
    pagination_class = CustomPagination
    queryset = Voter.objects.all()

    
       

    
    