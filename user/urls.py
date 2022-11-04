from django.urls import path
from .views import RegisterView, RoleListView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name="signup"),
    path("role/", RoleListView.as_view(), name="role")
   
]