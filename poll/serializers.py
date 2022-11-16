from rest_framework import serializers, fields
from poll.models import *
from utilities.models import Party, Candidate


class PollCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PollCategory
        fields = [
            
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
        
        
class CandidateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Candidate
        fields = ['name','candidate_picture','main_candidate']
        
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
        
        
           
        