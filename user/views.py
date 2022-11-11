from rest_framework.views import APIView
from .serializers import RegisterSerializer, RoleSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .models import User, Role
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import ListAPIView
from rest_framework import status
from .tokens import create_jwt_pair_for_user

from django.contrib.auth import authenticate
from rest_framework.request import Request

from .permissions import IsAdmin, IsSuperAdmin
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    serializer_class= RegisterSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    
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
        
        
class LoginView(APIView):
    def post(self, request:Request):
        email=request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message": "Login Successful",
                "token": tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"}, status=status.HTTP_403_FORBIDDEN)
        
        
    def get(self, request:Request):
        content = {
            "user":str(request.user),
            "auth": str(request.auth)
        }
        
        return Response(data=content, status=status.HTTP_200_OK)

            
        
class RoleListView(ListAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
