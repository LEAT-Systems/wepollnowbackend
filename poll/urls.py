from urllib.parse import urlparse
from poll.views import *
from django.urls import path

urlpatterns = [
    path('user_polls/', GetPollsForVoter.as_view(), name="user_polls"),
    path('poll_candidates/', GetPollCategory.as_view(), name="poll_candidates")
]
