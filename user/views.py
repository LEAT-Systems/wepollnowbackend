from rest_framework.views import APIView
from .serializers import RegisterSerializer, RoleSerializer, UserSerializer, ChangePasswordSerializer, UserRUDSerializer
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

from rest_framework.generics import UpdateAPIView

from rest_framework.generics import GenericAPIView
from rest_framework import mixins




import random
import string

def get_random_password():
    random_source = string.ascii_letters + string.digits 
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    

    # generate other characters
    for i in range(5):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password



class RegisterView(APIView):
    serializer_class= RegisterSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    
    def post(self, request):
        admin_group, created = Group.objects.get_or_create(name="AdminUser")
        
        content_type = ContentType.objects.get_for_model(User)
        post_permission = Permission.objects.filter(content_type=content_type)
        
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                role = request.data.get("role", None)
                if role is not None:
                    password = get_random_password()
                    print(password)
                    if role == "ADMIN":
                        user = User.objects.create_user(**serializer.validated_data, password = password, is_staff=True)
                        
                        for perm in post_permission:
                            if perm.codename == "view_user":
                                admin_group.permissions.add(perm)
                                
                        user.groups.add(admin_group)
                        return Response({'Success': "Admin created", "password": password}, status=status.HTTP_201_CREATED)
                    else:
                        user = User.objects.create_superuser(**serializer.validated_data, password = password)
                        return Response({'Success': "Super Admin created", "password": password}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'Error': "Provide role for staff"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'Error': "Invalid Data Provided"}, status=status.HTTP_400_BAD_REQUEST)
        except (Exception):
            return Response({"error": "Something Went wrong"}, status=status.HTTP_400_BAD_REQUEST)  


class LoginView(APIView):
    def post(self, request:Request):
        email=request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message": "Login Successful",
                "token": tokens,
                "name": user.name
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

class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAdmin]

    def get_object(self):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"message": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status" : "success",
                "code": status.HTTP_200_OK,
                "message" : "Password updated successfully"
            }

            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
class AdminListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AdminRetrieveUpdateDeleteView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserRUDSerializer
    queryset = User.objects.all()

    def get(self, request:Request, *args, **kwargs):

        return self.retrieve(request, *args, **kwargs) 
    
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

class RoleListView(ListAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
