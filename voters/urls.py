from voters.views import *
from django.urls import path

urlpatterns = [
    path('', voters),
    path('<int:pk>', voter_by_id )
]