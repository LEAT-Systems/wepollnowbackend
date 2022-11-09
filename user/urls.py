from django.urls import path
from .views import RegisterView, RoleListView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', RegisterView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("role/", RoleListView.as_view(), name="role"),
    
   
]