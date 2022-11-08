from audioop import maxpp
from django.db import models

import uuid

# Create your models here.
class Voter(models.Model):
    device_id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    valid_voters_card = models.BooleanField(default="False")
    residential_status = models.BooleanField(default="True")
    state_of_origin = models.ForeignKey("utilities.State",blank=True, null=True, on_delete=models.CASCADE, related_name= "stateOfOrigin")
    resident_state = models.ForeignKey("utilities.State",blank=True, null=True, on_delete=models.CASCADE, related_name= "stateOfResidence")
    resident_lga = models.ForeignKey("utilities.Lga", blank=True, null=True, on_delete=models.CASCADE, related_name= "lgaOfResidence")
    age_range = models.IntegerField()
    gender = models.IntegerField()
    marital_status = models.IntegerField()
    religion = models.IntegerField()
    employment_status = models.IntegerField()
    accomodation_status = models.IntegerField()
    first_time_voter = models.BooleanField(default="False")
    diaspora_voter = models.BooleanField(default="False")


    def __str__(self):
        return self.contact


class Vote(models.Model):
    voter = models.ForeignKey(Voter, blank=False, null=False, on_delete=models.CASCADE)
    candidate = models.OneToOneField("utilities.Candidate", blank=False, null=False, on_delete=models.CASCADE)
    poll = models.ForeignKey("poll.Poll", on_delete=models.CASCADE, blank=False, null=False)
    voted_at = models.DateTimeField()

    def __str__(self):
        return self.contact
