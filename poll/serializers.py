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
        fields = ['id','name', 'partyCandidate']
        
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
        fields = ['id','name', 'partyCandidate']
        
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
    party_votes_count = serializers.SerializerMethodField(read_only =True)
    

    class Meta:
        model = Party
        fields = "__all__"

    def get_voteCount(self,obj):
        poll_id = self.context["poll_id"]
        vote_count = obj.party_votes.filter(poll__id=poll_id)
        #vote_count = vote_count.filter(voter__gender=2)
        #vote_count = vote_count.filter(voter__marital_status=3)
        return vote_count.count()

    def get_party_votes_count(self, obj):
        poll_id = self.context["poll_id"]
        return PartyVoteSerializer(obj.party_votes_count.filter(poll__id=poll_id), many=True).data

        
           
        