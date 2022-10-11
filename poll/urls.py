from urllib.parse import urlparse
from poll.views import *
from django.urls import path

urlpatterns = [
    path('', add_poll_category)
]