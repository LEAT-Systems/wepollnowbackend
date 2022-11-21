import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from poll.models import *
from poll.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView 
from voters.models import Voter
from django.db.models import Q
from utilities.models import Lga, Party, Candidate, State, Senatorial
from rest_framework.views import APIView
from rest_framework import status




class PollCategoryList(ListAPIView):
    serializer_class =PollCategorySerializer
    queryset = PollCategory.objects.all()

class CandidatesList(ListAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

class Polls(CreateAPIView):
    serializer_class = CreatePollSerializer
    queryset = Poll.objects.all()

class AllPollsList(ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
        

class GetPollsForVoters(APIView):
    serializer_class = PollSerializer
    
    def post(self, request, format=None):
        try :
            if self.request.data.get("voter_id"): 
                voter_id = self.request.data["voter_id"]
                voter = Voter.objects.get(id = voter_id)
                if voter.resident_state is None:
                    polls = Poll.objects.filter(poll_category__id = 1)

                    serializer = PollSerializer(polls, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    lga = Lga.objects.get(id=voter.resident_lga.id)
                    senatorial_id = lga.senatorial_id
                    
                    polls = Poll.objects.filter(Q(poll_category__id = 1 ) | (Q(poll_category__id=3) & Q(poll_senatorial_district=senatorial_id.id))  | (Q(poll_category__id=2) & Q(poll_state=voter.resident_state.id)))
                    serializer = PollSerializer(polls, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                polls = Poll.objects.filter(Q(poll_category__id = 1 ) | (Q(poll_category__id=2) & Q(poll_state=25)) | (Q(poll_category__id=2) & Q(poll_state=33))| (Q(poll_category__id=2) & Q(poll_state=9)))
                serializer = PollSerializer(polls, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except (Exception):
            return Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)     
       
          


class GetPollPartiesAndCandidates(APIView):
    serializer_class  = PollPartySerializer

    def post(self, request):
        try :
            poll_id = self.request.data["poll_id"]
            pollParties = Party.objects.filter(poll_parties__id=poll_id)
            context = {
                "poll_id" : poll_id
            }
            serializer = PollPartySerializer(pollParties, many=True, context = context)
            return Response(serializer.data)
        except (Exception):
            return Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)           


class GetPartiesAndCandidatesForPollCategory(APIView):
    serializer_class  = PollCategoryPartySerializer

    def post(self, request):
        try:
            pollcategory_id = self.request.data["pollcategory_id"]
            poll_category = PollCategory.objects.get(id = pollcategory_id)
            context = { }

            if self.request.data.get("state_id"):
                state_id = self.request.data["state_id"]
                state = State.objects.get(id = state_id)
                pollParties = Party.objects.filter(party_candidate__poll_category=poll_category, party_candidate__state_id = state).prefetch_related("party_candidate").distinct()        

                context["state_id"]=state_id
                
                    
            else:
                senatorial_id = self.request.data["senatorial_id"]
                senatorial = Senatorial.objects.get(id=senatorial_id)
                pollParties = Party.objects.filter(party_candidate__poll_category=poll_category, party_candidate__senatorial_id = senatorial).prefetch_related("party_candidate").distinct()        

                context["senatorial_id"] = senatorial_id
                
                

            context['pollcategory_id'] = pollcategory_id

            serializer = PollCategoryPartySerializer(pollParties, many=True, context = context)
            return Response(serializer.data)
            
        except (Exception):
            return Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST) 

 



       
        









        
