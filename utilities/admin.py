from django.contrib import admin
from .models import Subscriber, Lga, State, Senatorial, Candidate

admin.site.register(Subscriber)
admin.site.register(State)
admin.site.register(Senatorial)
admin.site.register(Lga)
admin.site.register(Candidate)
