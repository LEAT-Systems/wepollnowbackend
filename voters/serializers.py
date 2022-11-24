from rest_framework import serializers
from voters.models import *
from utilities.models import State, Lga, Party
from poll.models import Votes, Poll, VoteCount
from rest_framework.validators import ValidationError
from rest_framework.response import Response
from rest_framework import status



class PartySerializer(serializers.ModelSerializer):

    class Meta:
        model = Party
        fields = "__all__"

class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = State
        fields = "__all__"
        
class LgaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lga
        fields = "__all__"


class PollSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Poll
        fields = "__all__"


class VoterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    state_of_origin_id = serializers.IntegerField(write_only=True)
    state_of_origin =StateSerializer(read_only=True)
    
    resident_state_id = serializers.IntegerField(write_only=True,required=False )
    resident_state = StateSerializer(read_only=True)
    
    resident_lga_id = serializers.IntegerField(write_only=True, required=False)
    resident_lga = LgaSerializer(read_only=True)
    
    class Meta:
        model = Voter
       
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    voter_id = serializers.UUIDField(write_only=True)
    voter =VoterSerializer(read_only=True)
    
    party_id = serializers.IntegerField(write_only=True)
    party = PartySerializer(read_only=True)
    
    poll_id = serializers.IntegerField(write_only=True)
    poll = PollSerializer(read_only=True)
    
    class Meta:
        model = Votes
       
        fields = "__all__"

    def validate(self, attrs):
        voter = Voter.objects.get(id=attrs['voter_id'])
        poll = Poll.objects.get(id=attrs['poll_id'])
        party = Party.objects.get(id=attrs['party_id'])

       
        votess = Votes.objects.filter(poll=poll, voter=voter).exists()
        if votess:
            raise ValidationError("You have voted already for this poll")
        else:
            voteCount, created = VoteCount.objects.get_or_create(
                poll=poll, party=party
            )
            voteCount.vote_count +=1
            voteCount.save()


        return super().validate(attrs)



        

        
