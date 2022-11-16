import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from poll.models import *
from poll.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView
from voters.models import Voter
from django.db.models import Q
from utilities.models import Lga, Party
   
        
class GetPollsForVoter(ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    
    def get_queryset(self):
        voter_id = self.request.data.get("voter_id", None)
        if voter_id: 
            voter = Voter.objects.get(id = voter_id)
            if voter.resident_state is None:
                polls = Poll.objects.filter(poll_category__id = 1)

                return polls
            else:
                lga = Lga.objects.get(id=voter.resident_lga.id)
                senatorial_id = lga.senatorial_id
                
                polls = Poll.objects.filter(Q(poll_category__id = 1 ) | (Q(poll_category__id=3) & Q(poll_senatorial_district=senatorial_id.id))  | (Q(poll_category__id=2) & Q(poll_state=voter.resident_state.id)))
                return polls
        else:
                polls = Poll.objects.filter(Q(poll_category__id = 1 ) | (Q(poll_category__id=2) & Q(poll_state=25)) | (Q(poll_category__id=2) & Q(poll_state=33))| (Q(poll_category__id=2) & Q(poll_state=9)))
                return polls

        
class GetPollCategory(ListAPIView):
    serializer_class  = PollPartySerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['poll_id'] = self.request.data['poll_id']   
        return context
    
    def get_queryset(self):
        poll_id =  self.request.data['poll_id']
        pollParties = Party.objects.filter(poll_parties__id=poll_id)
        print(pollParties)
        return pollParties
        
        
        
