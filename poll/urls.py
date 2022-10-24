from urllib.parse import urlparse
from poll.views import *
from django.urls import path

urlpatterns = [
    path('', poll),
    path('get_categories', poll_category)
]