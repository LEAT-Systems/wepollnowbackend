import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from poll.models import *
from poll.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView
from voters.models import Voter
from django.db.models import Q
from utilities.models import Lga
   

# @api_view(['GET', 'POST'])
# def poll(request):
#     if request.method == 'GET':
#         poll_category = request.query_params.get('category')
#         state_id = request.query_params.get('state')
#         if poll_category == 1:
#             poll_data = Poll.objects.filter(poll_category = poll_category)
#             serialized_data = PollOutputSerializer(poll_data, many=True)
#             return Response(serialized_data.data)
#         elif poll_category == 2:
#             poll_data = Poll.objects.filter(poll_category = poll_category, poll_state = state_id)
#             serialized_data = PollOutputSerializer(poll_data, many=True)
#             return Response(serialized_data.data)
#         poll_data = Poll.objects.filter(poll_category = poll_category, poll_state = state_id)
#         serialized_data = PollOutputSerializer(poll_data, many=True)
#         return Response(serialized_data.data)
    
#     if request.method == 'POST':
#         serialized_data = PollInputSerializer(data=request.data)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response(serialized_data.data)
#         else:
#             return Response(serialized_data.errors)
        
        
class getPollsForVoter(ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    
    def get_queryset(self):
        voter_id = self.request.data.get("voter_id", None)
           
        voter = Voter.objects.get(id = voter_id)
        if voter.resident_state is None:
            polls = Poll.objects.filter(poll_category__id = 1)

            return polls
        else:
            lga = Lga.objects.get(id=voter.resident_lga.id)
            senatorial_id = lga.senatorial_id
            
            polls = Poll.objects.filter(Q(poll_category__id = 1 ) | (Q(poll_category__id=3) & Q(poll_senatorial_district=senatorial_id.id))  | (Q(poll_category__id=2) & Q(poll_state=voter.resident_state.id)))
            return polls

        
        
        
        
        
