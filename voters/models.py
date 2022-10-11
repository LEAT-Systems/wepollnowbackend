from django.db import models

# Create your models here.
class Voter(models.Model):
    contact = models.CharField(max_length=11)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=15, blank=True)
    mac_address = models.CharField(max_length=30, blank=True)
    valid_voters_card = models.BooleanField(default="False")
    residential_status = models.BooleanField(default="True")
    resident_state_id = models.IntegerField(blank=True)
    resident_lga_id = models.IntegerField(blank=True)


    def __str__(self):
        return self.contact


class Vote(models.Model):
    contact = models.CharField(max_length=11)
    poll_id = models.CharField(max_length=15)
    voted_at = models.DateTimeField()

    def __str__(self):
        return self.contact
