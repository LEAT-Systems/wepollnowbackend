
from rest_framework import serializers
from utilities.models import *


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
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