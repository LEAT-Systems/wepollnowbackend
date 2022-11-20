
from rest_framework import serializers
from utilities.models import *



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

class LgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lga
        fields = [
            'id',
            'name',
            'state_id',
            'senatorial_id'
        ]
        
class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = Contact
        fields = [
            'name',
            'message',
            'email'
        ]


class SubscriberSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = Subscriber
        fields = [
            'id',
            'email'
        ]

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            'id',
            'name',
            'poll',
            'poll_category',
            'party',
            'state_id',
            'senatorial_id',
            'main_candidate',
            'candidate_picture'
        ]

