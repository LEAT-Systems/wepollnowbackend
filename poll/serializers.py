from rest_framework import serializers, fields
from poll.models import *


class PollCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PollCategory
        fields = [
            'id',
            'title',
            'poll_description',
            'created_date',
            'updated_date'
        ]


class PollOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'id',
            'poll_category',
            'poll_date',
            'poll_state',
        ]

class PollInputSerializer(serializers.ModelSerializer):
    poll_date = fields.DateField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    class Meta:
        model = Poll
        fields = [
            'id',
            'poll_category',
            'poll_state',
            'poll_date',
            'poll_senatorial_district',
            'poll_lga',
        ]
