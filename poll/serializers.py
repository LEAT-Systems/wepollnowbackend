from rest_framework import serializers, fields
from poll.models import *
from utilities.models import Party, Candidate, State,Senatorial
from voters.models import Voter
from datetime import date
from datetime import datetime



class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = [
            'id',
            'name'
        ]


class SenatorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senatorial
        fields = [
            'id',
            'name',
            'state_id'
        ]

class SurveyCategoryCreateSerializer(serializers.ModelSerializer):
    survey_name = serializers.ListField(child=serializers.CharField(), write_only=True)
    surveyName = serializers.CharField(required=False)

    class Meta:
        model = SurveyCategory
        fields = "__all__"

    def create(self, validated_data):
        surveyName = validated_data.pop('survey_name', [])
        if surveyName:
            for name in surveyName:
                survey_category = SurveyCategory.objects.create(surveyName = name)

        return survey_category

    
    

class SurveyCategoryRetrieveSerializer(serializers.ModelSerializer):
    response_count = serializers.SerializerMethodField()
    percentage = serializers.SerializerMethodField()
    class Meta:
        model = SurveyCategory
        fields = "__all__"

    def get_response_count(self, obj):
        poll_id = self.context["poll_id"]
        category_count = obj.survey_category.filter(poll__id=poll_id).count()
        return category_count


    def get_percentage(self, obj):
        poll_id = self.context["poll_id"]
        totalResponse = SurveyResponse.objects.filter(poll__id=poll_id).count()
        
        value = self.get_response_count(obj)
        try:
            percent = (value/totalResponse) * 100
            return round(percent, 1)
        except Exception:
            return 0
        

class SurveyCategoryRudSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SurveyCategory
        fields = "__all__"

class SurveyResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyResponse
        fields = "__all__"



class PollCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PollCategory
        fields = [
            'id',
            'title'
           
        ]




class PollSerializer(serializers.ModelSerializer):
    poll_category = PollCategorySerializer(read_only = True)
    poll_date =  serializers.DateTimeField()
    poll_state_name = serializers.CharField(source='poll_state')
    poll_senatorial_district_name = serializers.CharField(source="poll_senatorial_district")
    class Meta:
        model = Poll
        fields = [
            'id',
            'poll_category',
            'poll_name',
            'poll_state',
            'poll_state_name',
            'poll_date',
            'poll_senatorial_district',
            'poll_senatorial_district_name',
            'poll_startDate',
            'poll_endDate',
            'status'
            
        ]
    


class CreatePollSerializer(serializers.ModelSerializer):
    poll_startDate = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    poll_endDate = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    poll_state_id = serializers.IntegerField(required=False)
    poll_senatorial_district_id =  serializers.IntegerField(required=False)
    poll_category_id = serializers.IntegerField()
    party = serializers.PrimaryKeyRelatedField(queryset = Party.objects.all(), many = True, write_only=True)
    candidate = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    
    class Meta:
        model = Poll
        fields =  [
            'poll_category_id',
            'poll_name',
            'poll_senatorial_district_id',
            'poll_senatorial_district',
            'poll_state_id',
            'poll_state',
            'poll_startDate',
            'poll_endDate',
            'status',
            'party',
            'candidate'        
        ]

    
    def create(self, validated_data):
        partyid = validated_data.pop('party', [])
        state_id = validated_data.pop('poll_state_id', None)
        senatorial_id = validated_data.pop('poll_senatorial_district_id', None)
        candidate = validated_data.pop('candidate', [])
        if state_id is not None:
            state = State.objects.get(id=state_id)
        if senatorial_id is not None:
            senatorial = Senatorial.objects.get(id=senatorial_id)
        poll_category_id = validated_data.pop('poll_category_id')
        pollCategory = PollCategory.objects.get(id=poll_category_id)

        if senatorial_id and state_id:
            poll = Poll.objects.create(poll_category=pollCategory, poll_state=state, poll_senatorial_district= senatorial, **validated_data)

        elif state_id is not None:
            poll = Poll.objects.create(poll_category=pollCategory, poll_state=state, **validated_data)
        
        else:
            poll = Poll.objects.create(poll_category=pollCategory, **validated_data)

        for party in partyid:
            poll.party.add(party)
        
        for id in candidate:
             candidateObject = Candidate.objects.get(id=id)
             candidateObject.poll= poll
             candidateObject.save()
    

        return poll

class PollSerializer(serializers.ModelSerializer):
    poll_startDate = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    poll_endDate = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    poll_state_id = serializers.IntegerField(required=False)
    poll_state = StateSerializer(read_only = True)
    poll_senatorial_district_id=  serializers.IntegerField(required=False)
    poll_senatorial_district =SenatorialSerializer(read_only=True)
    poll_category_id = serializers.IntegerField(write_only=True)
    poll_category = PollCategorySerializer(read_only=True)
    party = serializers.PrimaryKeyRelatedField(queryset = Party.objects.all(), many = True, write_only=True)
    candidate = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    
    class Meta:
        model = Poll
        fields =  "__all__"

    def update(self, instance, validated_data):
        candidate = validated_data.pop('candidate', [])
        instance = super().update(instance, validated_data)
        if candidate:
            instance.poll_candidate.clear()
        for id in candidate:
             candidateObject = Candidate.objects.get(id=id)
             candidateObject.poll= instance
             candidateObject.save()
        return instance 
      
        
class CandidateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Candidate
        fields = ['id','name','candidate_picture','main_candidate']
        
class PollPartySerializer(serializers.ModelSerializer):
    partyCandidate = serializers.SerializerMethodField(read_only=True)

    
    class Meta:
        model = Party
        fields = ['id','name', 'partyCandidate', 'logo']
        
    def get_partyCandidate(self, obj):
        poll_id = self.context["poll_id"]
        candidate = CandidateSerializer(obj.party_candidate.filter(poll__id=poll_id), many=True).data
        return candidate
   
        
class CandidateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Candidate
        fields = ['id','name','candidate_picture','main_candidate']

        
        
class PollCategoryPartySerializer(serializers.ModelSerializer):
    partyCandidate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Party
        fields = ['id','name', 'partyCandidate', 'logo']
        
    def get_partyCandidate(self, obj):
        pollcategory_id = self.context["pollcategory_id"]
        state_id = self.context.get("state_id", None)
        senatorial_id = self.context.get("senatorial_id", None)
        if state_id:
            candidate = CandidateSerializer(obj.party_candidate.filter(poll_category__id=pollcategory_id, state_id__id=state_id), many=True).data
        elif senatorial_id :
            candidate = CandidateSerializer(obj.party_candidate.filter(poll_category__id=pollcategory_id, senatorial_id__id=senatorial_id), many=True).data

        else :
            candidate = CandidateSerializer(obj.party_candidate.filter(poll_category__id=pollcategory_id), many=True).data
      
        return candidate


class PartyVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteCount
        fields = ['vote_count']

class PollDetailSerializer(serializers.ModelSerializer):
    poll_category = PollCategorySerializer(read_only = True)
    poll_date =  serializers.DateTimeField()
    poll_state_name = serializers.CharField(source='poll_state')
    poll_senatorial_district_name = serializers.CharField(source="poll_senatorial_district")
    class Meta:
        model = Poll
        fields = [
            'id',
            'poll_category',
            'poll_name',
            'poll_state',
            'poll_state_name',
            'poll_date',
            'poll_senatorial_district',
            'poll_senatorial_district_name',
            'poll_startDate',
            'poll_endDate',
            'status'
            
        ]
 
class PollPartyResultSerializer(serializers.ModelSerializer):
    voteCount = serializers.SerializerMethodField(read_only=True)
    partyCandidate = serializers.SerializerMethodField(read_only=True)
    votePercent = serializers.SerializerMethodField()
    poll_details = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Party
        fields = "__all__"


    def get_poll_details(self,obj):
        poll_id = self.context["poll_id"]
        poll = PollDetailSerializer(Poll.objects.get(id=poll_id)).data
        return poll


    def get_voteCount(self,obj):
        poll_id = self.context["poll_id"]
        vote_count = obj.party_votes.filter(poll__id=poll_id)
        return vote_count.count()
    
    def get_partyCandidate(self, obj):
        poll_id = self.context["poll_id"]
        candidate = CandidateSerializer(obj.party_candidate.filter(poll__id=poll_id), many=True).data
        return candidate

    def get_votePercent(self, obj):
        poll_id = self.context["poll_id"]
        totalPollVote = Votes.objects.filter(poll__id=poll_id).count()
        value = self.get_voteCount(obj)
        try:
            percent = (value/totalPollVote) * 100
            return round(percent, 1)
        except Exception:
            return 0
        

    def get_party_votes_count(self, obj):
        poll_id = self.context["poll_id"]
        return PartyVoteSerializer(obj.party_votes_count.filter(poll__id=poll_id), many=True).data

class PollPartyResultFilterSerializer(serializers.ModelSerializer):
    voteCount = serializers.SerializerMethodField(read_only=True)
    partyCandidate = serializers.SerializerMethodField(read_only=True)
    votePercent = serializers.SerializerMethodField()


    class Meta:
        model = Party
        fields = "__all__"

    def get_voteCount(self,obj):
        poll_id = self.context["poll_id"]
        gender = self.context.get("gender", None)
        firstTimeVOter = self.context.get("firstTimeVOter",None)
        diaspora_voter = self.context.get("diaspora_voter", None)
        residence_state = self.context.get("residence_state", None)
        residence_lga= self.context.get("residence_lga", None)
        state_of_origin = self.context.get("state_of_origin", None)
        age_range = self.context.get("age_range", None)
        religion = self.context.get("religion", None)
        marital_status = self.context.get("marital_status", None)
        employment_status = self.context.get("employment_status", None)
        property_status = self.context.get("property_status", None)
        country = self.context.get("country", None)

        vote_count = obj.party_votes.filter(poll__id=poll_id)
        if gender:
            vote_count = vote_count.filter(voter__gender=gender)
        if firstTimeVOter:
            vote_count = vote_count.filter(voter__first_time_voter=firstTimeVOter)
        if diaspora_voter:
            vote_count = vote_count.filter(voter__diaspora_voter=diaspora_voter)
        if residence_state:
            vote_count = vote_count.filter(voter__resident_state=residence_state)
        if residence_lga:
            vote_count = vote_count.filter(voter__resident_lga=residence_lga)
        if state_of_origin:
            vote_count = vote_count.filter(voter__state_of_origin=state_of_origin)
        if age_range:
            vote_count = vote_count.filter(voter__age_range=age_range)
        if religion:
            vote_count = vote_count.filter(voter__religion=religion)
        if employment_status:
            vote_count = vote_count.filter(voter__employment_status=employment_status)
        if marital_status:
            vote_count = vote_count.filter(voter__marital_status=marital_status)
        
        if country:
            vote_count = vote_count.filter(voter__country=country)
        
        if property_status:
            vote_count = vote_count.filter(voter__property_status=property_status)

        return vote_count.count()


    def get_partyCandidate(self, obj):
        poll_id = self.context["poll_id"]
        candidate = CandidateSerializer(obj.party_candidate.filter(poll__id=poll_id), many=True).data
        return candidate
    
    def get_votePercent(self, obj):
        poll_id = self.context["poll_id"]
        totalPollVote = Votes.objects.filter(poll__id=poll_id).count()
        value = self.get_voteCount(obj)
        try:
            percent = (value/totalPollVote) * 100
            return round(percent, 1)
        except Exception:
            return 0

class VoterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Voter
       
        fields = ["resident_state", "resident_lga"]



class PartyCandidateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Candidate
        fields = ['name']
     

class PartySerializer(serializers.ModelSerializer):
    party_candidate = serializers.SerializerMethodField(read_only = True)
    

    class Meta:
        model = Party
        fields = "__all__"

    def get_party_candidate(self, obj):
        poll_id = self.context["pk"]
        candidate = PartyCandidateSerializer(obj.party_candidate.filter(poll__id=poll_id,main_candidate=True), many=True).data
        return candidate


class VoteSerializer(serializers.ModelSerializer):
    voter = VoterSerializer(read_only = True)
    party = PartySerializer(read_only = True)

    class Meta:
        model = Votes
        fields = ["voter", "party"]


class PollPartyResultCandidateSerializer(serializers.ModelSerializer):
    poll_votes = VoteSerializer(many=True, read_only =True)

    class Meta:
        model = Poll
        fields = ["poll_name", "poll_category", "poll_votes"]


class PollStatusCountSerializer(serializers.ModelSerializer):
    scheduledPolls = serializers.SerializerMethodField(read_only=True)
    ongoingPolls = serializers.SerializerMethodField(read_only=True)
    concludedPolls = serializers.SerializerMethodField(read_only=True)
    allUsers = serializers.SerializerMethodField(read_only=True)
    newUsers = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = PollCategory
        fields = ['scheduledPolls', 'ongoingPolls', 'concludedPolls', 'allUsers', 'newUsers']

    def get_scheduledPolls(self, obj):
        upcoming = Poll.objects.filter(poll_startDate__date__gt = date.today()).count()
        return upcoming

    def get_concludedPolls(self, obj):
        concluded = Poll.objects.filter(poll_endDate__date__lt = date.today()).count()
        return concluded

    def get_ongoingPolls(self,obj):
        ongoing = Poll.objects.filter(poll_startDate__date__lte = date.today(), poll_endDate__date__gte = date.today()).count()
        return ongoing
    
    def get_allUsers(self,obj):
        voter = Voter.objects.all().count()
        return voter

    def get_newUsers(self,obj):
        voter = Voter.objects.filter(date_reg__date = date.today()).count()
        return voter