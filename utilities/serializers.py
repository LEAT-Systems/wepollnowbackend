
from rest_framework import serializers
from utilities.models import *
from poll.serializers import PollCategorySerializer



class WebHitsSerializer(serializers.ModelSerializer):
    view_hits = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Hit
        fields = ['view_hits', 'ip', 'date']

    def validate(self, attrs):
        return super().validate(attrs)
    
    def get_view_hits(self, obj):
        try:
            return obj.hit_count.hits
        except:
            pass

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

class ConstituencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Constituency
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
            'senatorial_id',
            'constituency_id'
        ]
        
class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = Contact
        fields = [
            'id',
            'name',
            'message',
            'email',
            'created_date'
        ]


class SubscriberSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = Subscriber
        fields = [
            'id',
            'email',
            'created_date'
        ]

class PartySerializer(serializers.ModelSerializer):

    class Meta:
        model = Party
        fields = [
            'id',
            'name',
            'abbr',
            'logo'
        ]

class CandidateSerializer(serializers.ModelSerializer): 
    poll_category_id = serializers.IntegerField(write_only=True)
    poll_category = PollCategorySerializer(read_only=True)

    party_id = serializers.IntegerField(write_only=True)
    party = PartySerializer(read_only = True)

    state_id_id = serializers.IntegerField(write_only=True, required=False)
    state_id = StateSerializer(read_only=True)

    senatorial_id_id = serializers.IntegerField(write_only=True, required=False)
    senatorial_id = SenatorialSerializer(read_only=True)

    constituency_id_id = serializers.IntegerField(write_only=True, required=False)
    constituency_id = SenatorialSerializer(read_only=True)

    main_candidate = serializers.BooleanField()
    candidate_picture = serializers.ImageField(required=False)

    poll = serializers.CharField(read_only=True)



    class Meta:
        model = Candidate
        fields = [
            'id',
            'name',
            'poll',
            'poll_category',
            'poll_category_id',
            'party_id',
            'party',
            'state_id_id',
            'state_id',
            'senatorial_id',
            'senatorial_id_id',
            'constituency_id_id',
            'constituency_id',
            'main_candidate',
            'candidate_picture'
        ]



