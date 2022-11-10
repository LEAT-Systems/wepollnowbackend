from utilities.views import *
from utilities.seeder import *
from django.urls import path

urlpatterns = [
    path('states/', states),
    path('states/<int:pk>', states_by_id),
    path('senatorial/', senatorial),
    path('senatorial/<int:state_id>', senatorial_by_state),
    path('lga/', lga),
    path('lga/<int:state_id>', lga_by_state),
    path('lga/senatorial/<int:senatorial_id>', lga_by_senatorial),
    path('seed/lga', seed_lga),
    path('seed/states', seed_states),
    path('seed/senatorial', seed_senatorial)
]