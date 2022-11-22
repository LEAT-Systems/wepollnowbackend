from voters.views import *
from django.urls import path

urlpatterns = [
    path('', Voters.as_view(), name="createVoter"),
    path("vote/", Votes.as_view(), name="vote")
]