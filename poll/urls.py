from urllib.parse import urlparse
from poll.views import *
from django.urls import path

urlpatterns = [
    path('user_polls/', getPollsForVoter.as_view(), name="user_polls")
]
