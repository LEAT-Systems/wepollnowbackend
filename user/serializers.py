from rest_framework import serializers
from .models import Role

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    name = serializers.CharField()
    username = serializers.CharField()
    phone_number =serializers.CharField()
    


class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields =['id', 'roleName']
        

    
    

    