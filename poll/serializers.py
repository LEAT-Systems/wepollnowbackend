from rest_framework import serializers
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
