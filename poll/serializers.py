from rest_framework import serializers, fields
from poll.models import *
from utilities.models import Party, Candidate




class PollCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PollCategory
        fields = [
            'id',
            'title',
            'poll_description',
           
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
            'poll_lga',
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
        print(candidate[0])
        return candidate
        
        
           
        