from audioop import maxpp
from django.db import models
from utilities.models import *
import uuid

# Create your models here.

class Device(models.Model):
    device_ref = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    contact = models.CharField(max_length=11)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.contact

class Voter(models.Model):
    device_id = models.ForeignKey(Device, blank=False, null=False, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    valid_voters_card = models.BooleanField(default="False")
    residential_status = models.BooleanField(default="True")
    state_of_origin = models.IntegerField()
    resident_state = models.ForeignKey(States,blank=True, null=True, on_delete=models.CASCADE)
    resident_lga = models.ForeignKey(Lga, blank=True, null=True, on_delete=models.CASCADE)
    age_range = models.IntegerField()
    marital_status = models.IntegerField()
    employment_status = models.IntegerField()

    def __str__(self):
        return self.contact


class Vote(models.Model):
    voter = models.ForeignKey(Voter, blank=False, null=False, on_delete=models.CASCADE)
    poll_id = models.CharField(max_length=15)
    voted_at = models.DateTimeField()

    def __str__(self):
        return self.contact
