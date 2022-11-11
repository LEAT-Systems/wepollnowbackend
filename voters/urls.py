from voters.views import *
from django.urls import path

urlpatterns = [
    path('', Voters.as_view(), name="createVoter"),
]