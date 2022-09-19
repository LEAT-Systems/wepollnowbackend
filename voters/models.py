from django.db import models

# Create your models here.
class Voter(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.CharField(max_length=11)
    first_name = models.CharField(max_length=25)
    Last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=15)
    mac_address = models.CharField(max_length=30)
    valid_voters_card = models.BooleanField(default="False")
    residential_status = models.BooleanField(default="True")
    resident_state_id = models.IntegerField()
    resident_lga_id = models.IntegerField()


    def __str__(self):
        return self.contact


class Vote(models.Model):
    contact = models.CharField(max_length=11)
    poll_id = models.CharField(max_length=15)
    voted_at = models.DateTimeField()

    def __str__(self):
        return self.contact
