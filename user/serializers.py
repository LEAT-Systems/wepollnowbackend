from rest_framework import serializers
from .models import Role, User


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    username = serializers.CharField()
    phone_number = serializers.CharField(required=False)

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


    


class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields =['id', 'roleName']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

        
