from rest_framework import serializers, fields
from poll.models import *
from utilities.models import Party, Candidate




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
    class Meta:
        model = Poll
        fields = [
            'id',
            'poll_category',
            'poll_name',
            'poll_state',
            'poll_date',
            'poll_senatorial_district',
            'poll_startDate',
            'poll_endDate',
            'status'
            
        ]

class PartySerializer(serializers.ModelSerializer):

    class Meta:
        model = Party
        fields = "__all__"

class CreatePollSerializer(serializers.ModelSerializer):
    poll_startDate = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    poll_endDate = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    poll_state = serializers.IntegerField(required=False)
    poll_senatorial_district =  serializers.IntegerField(required=False)
    poll_category_id = serializers.IntegerField()
    party = serializers.PrimaryKeyRelatedField(queryset = Party.objects.all(), many = True, write_only=True)
    candidate = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    
    class Meta:
        model = Poll
        fields =  [
            'poll_category_id',
            'poll_name',
            'poll_senatorial_district',
            'poll_state',
            'poll_startDate',
            'poll_endDate',
            'status',
            'party',
            'candidate'
            
        ]
    
    def create(self, validated_data):
        partyid = validated_data.pop('party', [])
        candidate = validated_data.pop('candidate', [])
        poll_category_id = validated_data.pop('poll_category_id')
        pollCategory = PollCategory.objects.get(id=poll_category_id)
        print(pollCategory)
        poll = Poll.objects.create(poll_category=pollCategory, **validated_data)
        for party in partyid:
            poll.party.add(party)
        
        for id in candidate:
             candidateObject = Candidate.objects.get(id=id)
             candidateObject.poll= poll
             candidateObject.save()
    

        return poll
        
        
        
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



class PollPartyResultSerializer(serializers.ModelSerializer):
    voteCount = serializers.SerializerMethodField(read_only=True)
    #party_votes_count = serializers.SerializerMethodField(read_only =True)
    partyCandidate = serializers.SerializerMethodField(read_only=True)
    votePercent = serializers.SerializerMethodField()


    class Meta:
        model = Party
        fields = "__all__"

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
        percent = (value/totalPollVote) * 100
        return round(percent, 1)

    # def get_party_votes_count(self, obj):
    #     poll_id = self.context["poll_id"]
    #     return PartyVoteSerializer(obj.party_votes_count.filter(poll__id=poll_id), many=True).data

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
        if property_status:
            vote_count = vote_count.filter(voter__property_status=property_status)
        return vote_count.count()

    # def get_party_votes_count(self, obj):
    #     poll_id = self.context["poll_id"]
    #     return PartyVoteSerializer(obj.party_votes_count.filter(poll__id=poll_id), many=True).data

    def get_partyCandidate(self, obj):
        poll_id = self.context["poll_id"]
        candidate = CandidateSerializer(obj.party_candidate.filter(poll__id=poll_id), many=True).data
        return candidate
    
    def get_votePercent(self, obj):
        poll_id = self.context["poll_id"]
        totalPollVote = Votes.objects.filter(poll__id=poll_id).count()
        value = self.get_voteCount(obj)
        percent = (value/totalPollVote) * 100
        return round(percent, 1)
        
           
        