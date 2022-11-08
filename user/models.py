from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid


ROLE_CHOICES = (
    ('ADMIN', 'ADMIN'),
    ('SUPERADMIN', 'SUPERADMIN'),
)

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email field is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("SuperUser has to have is_staff being True")
    
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("SuperUser has to have is_superuser being True")
        
        return self.create_user(email=email, password=password, **extra_fields)
        


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=23)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    
    USERNAME_FIELD = "email"
    objects = CustomUserManager()
    REQUIRED_FIELDS = ['username', 'name', 'phone_number']
    
    def __str__(self):
        return self.email
    
    
class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    roleName = models.CharField(choices=ROLE_CHOICES, max_length=11)
    
    def __str__(self):
        return self.roleName
