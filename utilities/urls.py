from utilities.views import *
from django.urls import path

urlpatterns = [
    path('states/', states),
    path('states/<int:pk>', states_by_id),
    path('senatorial/', senatorial),
    path('senatorial/<int:state_id>', senatorial_by_state),
    path('lga/', lga),
    path('lga/<int:state_id>', lga_by_state),
    path('lga/senatorial/<int:senatorial_id>', lga_by_senatorial)
]