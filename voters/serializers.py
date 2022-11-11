from rest_framework import serializers
from voters.models import *
from utilities.models import State, Lga


class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = State
        fields = "__all__"
        
class LgaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lga
        fields = "__all__"


class VoterSerializer(serializers.ModelSerializer):
    state_of_origin_id = serializers.IntegerField(write_only=True)
    state_of_origin =StateSerializer(read_only=True)
    
    resident_state_id = serializers.IntegerField(write_only=True,required=False )
    resident_state = StateSerializer(read_only=True)
    
    resident_lga_id = serializers.IntegerField(write_only=True, required=False)
    resident_lga = LgaSerializer(read_only=True)
    
    class Meta:
        model = Voter
       
        fields = "__all__"
