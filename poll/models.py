from django.db import models
from utilities.models import *
from voters.models import *
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here.
class PollCategory(models.Model):
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add='True')
    updated_date = models.DateTimeField(auto_now='True')

    def __str__(self):
        return self.title


class Poll(models.Model):
    poll_category = models.ForeignKey(PollCategory, blank=False, on_delete=models.CASCADE)
    poll_name = models.CharField(max_length=30, default="Presidential Election")
    poll_date = models.DateTimeField(auto_now_add='True')
    poll_state = models.IntegerField(blank=True, null=True)
    poll_senatorial_district = models.IntegerField(blank=True, null=True)
    poll_startDate = models.DateTimeField(default=timezone.now)
    poll_endDate = models.DateTimeField(default=timezone.now)
    party = models.ManyToManyField('utilities.Party', related_name="poll_parties")
    status = models.IntegerField(default=1)
    

    def __str__(self):
        return self.poll_name
    
    def clean(self):
        super().clean()
        if not (timezone.now() <= self.poll_startDate <= self.poll_endDate):
            raise ValidationError('End date has to be greater than start date')


class Votes(models.Model):
    poll = models.ForeignKey(Poll, blank=False, null=False, on_delete=models.CASCADE, related_name='poll_votes')
    voter = models.ForeignKey(Voter, blank=False, null=False, on_delete=models.CASCADE, related_name='voter_votes')
    party = models.ForeignKey('utilities.Party', blank=False, null=False, on_delete=models.CASCADE, related_name='party_votes')
    created_date = models.DateTimeField(auto_now_add='True')
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.party.name
