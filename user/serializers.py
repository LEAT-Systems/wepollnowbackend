from rest_framework import serializers
from .models import Role
from phonenumber_field.serializerfields import PhoneNumberField


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    name = serializers.CharField()
    username = serializers.CharField()
    phone_number = PhoneNumberField(region="NG")
    


class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields =['id', 'roleName']
        
