from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from voters.models import Voter
from voters.serializers import VoterSerializer, VoteSerializer
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from utilities.pagination import CustomPagination
from poll.models import Votes
from rest_framework.views import APIView
from rest_framework import status



class PhonenumberCheck(APIView):

    def post(self, request):
        phone_Number = request.data['phoneNumber']
        phoneNumber = phone_Number.replace(" ", "")

        if phoneNumber:
            if Voter.objects.filter(phone=phoneNumber).exists():
                voter = Voter.objects.get(phone=phoneNumber)
                voter_id = voter.id
                return Response({"message":"A registered Voter", "voter_id": voter_id}, status=status.HTTP_208_ALREADY_REPORTED)
            else:
                return Response( status=status.HTTP_200_OK)
        else:
            return Response({"message":"Please Input a phone number"}, status=status.HTTP_400_BAD_REQUEST)

    
class Voters(ListCreateAPIView):
    serializer_class = VoterSerializer
    pagination_class = CustomPagination
    queryset = Voter.objects.all()

class Votes(CreateAPIView):
    serializer_class = VoteSerializer
    queryset = Votes.objects.all()




    
       

    
    