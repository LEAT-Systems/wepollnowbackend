from rest_framework import serializers
from voters.models import *

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = [
            'contact',
            'first_name',
            'last_name',
            'email',
            'ip_address',
            'mac_address',
            'valid_voters_card',
            'residential_status',
            'resident_state_id',
            'resident_lga_id'
        ]
