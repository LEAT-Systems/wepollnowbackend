from urllib.parse import urlparse
from poll.views import *
from django.urls import path

urlpatterns = [
    path('poll_categories/', getPollsForVoter.as_view(), name="poll_categories")
]