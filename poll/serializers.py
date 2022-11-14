from rest_framework import serializers, fields
from poll.models import *


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
