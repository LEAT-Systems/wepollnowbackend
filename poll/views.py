import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from poll.models import *
from poll.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from voters.models import Voter
from django.db.models import Q
from utilities.models import Lga, Party, Candidate, State, Senatorial
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Count

from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

from utilities.pagination import CustomPagination



class SurveyCategoryView(CreateAPIView):
    queryset = SurveyCategory.objects.all()
    serializer_class = SurveyCategoryCreateSerializer

class SurveyCategoryListView(ListAPIView):
    queryset = SurveyCategory.objects.all()
    serializer_class = SurveyCategoryRetrieveSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['poll_id'] = self.kwargs['poll_id']
        return context

class AllSurveyCategoryListView(ListAPIView):
    queryset = SurveyCategory.objects.all()
    serializer_class = SurveyCategoryRudSerializer

class SurveyCategoryRetrieveUpdateDelete(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = SurveyCategoryRudSerializer
    queryset = SurveyCategory.objects.all()

    def get(self, request:Request, *args, **kwargs):

        return self.retrieve(request, *args, **kwargs) 
    
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

class SurveyResponseView(ListCreateAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer


class PollCategoryList(ListAPIView):
    serializer_class =PollCategorySerializer
    queryset = PollCategory.objects.all()

class CandidatesList(ListAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    pagination_class = CustomPagination

class Polls(CreateAPIView):
    serializer_class = CreatePollSerializer
    queryset = Poll.objects.all()

class PollRetrieveUpdateDelete(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()

    def get(self, request:Request, *args, **kwargs):

        return self.retrieve(request, *args, **kwargs) 
    
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 


class AllPollsList(ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    pagination_class = CustomPagination 

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
                    constituency_id = lga.constituency_id
                    
                    polls = Poll.objects.filter(Q(poll_category__id = 1 ) | (Q(poll_category__id=3) & Q(poll_senatorial_district__id=senatorial_id.id))  | (Q(poll_category__id=2) & Q(poll_state__id=voter.resident_state.id)) | (Q(poll_category__id=4) & Q(poll_constituency__id=constituency_id.id)))
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
            return Response({"error": "Invalid Data" }, status=status.HTTP_400_BAD_REQUEST)           


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
                
                    
            elif self.request.data.get("senatorial_id"):
                senatorial_id = self.request.data["senatorial_id"]
                senatorial = Senatorial.objects.get(id=senatorial_id)
                pollParties = Party.objects.filter(party_candidate__poll_category=poll_category, party_candidate__senatorial_id = senatorial).prefetch_related("party_candidate").distinct()        

                context["senatorial_id"] = senatorial_id
            
            else :
                pollParties = Party.objects.filter(party_candidate__poll_category=poll_category).distinct()        

            context['pollcategory_id'] = pollcategory_id

            serializer = PollCategoryPartySerializer(pollParties, many=True, context = context)
            return Response(serializer.data)
             
        except (Exception):
            return Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST) 

class PollResult(APIView):
    serializer_class  = PollPartyResultSerializer
    pagination_class = CustomPagination


    def post(self, request):
        try: 
            poll_id = self.request.data["poll_id"]
            pollParties = Party.objects.filter(poll_parties__id=poll_id).prefetch_related('party_votes', 'party_votes_count').annotate(number_of_votes=Count('party_votes')).order_by('-number_of_votes')
        
            context = {
                "poll_id" : poll_id
            }
            serializer = self.serializer_class(pollParties, many=True, context = context)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"No votes": []}, status=status.HTTP_200_OK) 


# class PollResult(ListAPIView):
#     serializer_class  = PollPartyResultSerializer
#     filter_backends = [ OrderingFilter]
#     #filter_class = PartyVoteFilters
#     ordering_fields = ('name')
#     #ordering = ('name')
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context['poll_id'] = self.kwargs['poll_id']
#         return context

#     def get_queryset(self):
#         pollParties = Party.objects.filter(poll_parties__id=self.kwargs['poll_id']).prefetch_related('party_votes', 'party_votes_count').annotate(number_of_votes=Count('party_votes')).order_by('number_of_votes')
#         return pollParties


class PollResultFilter(GenericAPIView):
    serializer_class  = PollPartyResultFilterSerializer
    filter_backends = [ OrderingFilter]
    pagination_class = CustomPagination
    #filter_class = PartyVoteFilters
    #ordering_fields = ('name')
    ordering = ('-id')

    def post(self, request):
        
        poll_id = self.request.data.get('poll_id', None)
        gender = self.request.data.get("gender", None)
        firstTimeVOter = self.request.data.get("firstTimeVOter",None)
        diaspora_voter = self.request.data.get("diaspora_voter", None)
        residence_state = self.request.data.get("residence_state", None)
        residence_lga= self.request.data.get("residence_lga", None)
        state_of_origin = self.request.data.get("state_of_origin", None)
        age_range = self.request.data.get("age_range", None)
        religion = self.request.data.get("religion", None)
        marital_status = self.request.data.get("marital_status", None)
        employment_status = self.request.data.get("employment_status", None)
        property_status = self.request.data.get("property_status", None)


        pollParties = Party.objects.filter(poll_parties__id=poll_id).prefetch_related('poll_parties', 'party_votes') #.order_by('name')
        
        context = {
            "poll_id" : poll_id,
            "firstTimeVOter" : firstTimeVOter,
            "gender" :gender,
            "diaspora_voter" : diaspora_voter,
            "residence_state" : residence_state,
            "residence_lga" : residence_lga,
            "state_of_origin" : state_of_origin,
            "age_range":age_range,
            "religion": religion,
            "marital_status": marital_status,
            "employment_status": employment_status,
            "property_status" :property_status
        }

        serializer = self.serializer_class(pollParties, many=True, context = context)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PollDetailResultView(ListAPIView):
    serializer_class = PollPartyResultCandidateSerializer
    queryset = Poll.objects.all()
    pagination_class = CustomPagination



    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['pk'] = self.kwargs['pk']
        return context

    def get_object(self):
        poll = Poll.objects.get(id=self.kwargs['pk'])
        return poll


          




               

    



       
        









        
