from rest_framework.views import APIView
from .serializers import RegisterSerializer, RoleSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .models import User, Role
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import ListAPIView
from rest_framework import status




class RegisterView(APIView):
    serializer_class= RegisterSerializer
    
    def post(self, request):
        admin_group, created = Group.objects.get_or_create(name="AdminUser")
        
        content_type = ContentType.objects.get_for_model(User)
        post_permission = Permission.objects.filter(content_type=content_type)
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            role = request.data.get("role", None)
            if role is not None:
                if role == "ADMIN":
                    user = User.objects.create_user(**serializer.validated_data, is_staff=True)
                    
                    for perm in post_permission:
                        if perm.codename == "view_user":
                            admin_group.permissions.add(perm)
                            
                    user.groups.add(admin_group)
                    return Response({'Success': "Admin created"}, status=status.HTTP_201_CREATED)
                else:
                    user = User.objects.create_superuser(**serializer.validated_data)
                    return Response({'Success': "Super Admin created"}, status=status.HTTP_201_CREATED)
            else:
                return Response({'Error': "Provide role for staff"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error': "Invalid Data Provided"}, status=status.HTTP_400_BAD_REQUEST)

            
            
            
            
        
class RoleListView(ListAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
