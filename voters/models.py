from django.db import models
from utilities.models import *

# Create your models here.
class Voter(models.Model):
    contact = models.CharField(max_length=11)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=30)
    valid_voters_card = models.BooleanField(default="False")
    residential_status = models.BooleanField(default="True")
    resident_state = models.ForeignKey(States,blank=True, null=True, on_delete=models.CASCADE)
    resident_lga = models.ForeignKey(Lga, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.contact


class Vote(models.Model):
    contact = models.CharField(max_length=11)
    poll_id = models.CharField(max_length=15)
    voted_at = models.DateTimeField()

    def __str__(self):
        return self.contact