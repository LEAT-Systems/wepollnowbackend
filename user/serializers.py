from rest_framework import serializers
from .models import Role, User


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    phone_number = serializers.CharField(required=False)

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.RegexField(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', required=True, error_messages={'required': 'Custom error message'})
    new_password = serializers.RegexField(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', required=True, error_messages={'required': 'Custom error message'})

 

    


class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields =['id', 'roleName']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

        
