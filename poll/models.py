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
    poll_name = models.CharField(max_length=40, default="Presidential Election")
    poll_date = models.DateTimeField(auto_now_add='True')
    poll_state = models.ForeignKey('utilities.State',blank=True, null=True, on_delete=models.SET_NULL, related_name='poll_state')
    poll_senatorial_district = models.ForeignKey('utilities.Senatorial', blank=True, null=True, on_delete=models.SET_NULL, related_name='poll_senatorial_district')
    poll_constituency = models.ForeignKey('utilities.Constituency', blank=True, null=True, on_delete=models.SET_NULL, related_name='poll_constituency')
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

    def __str__(self):
        return self.party.name

class VoteCount (models.Model):
    party = models.ForeignKey('utilities.Party', blank=False, null=False, on_delete=models.CASCADE, related_name='party_votes_count')
    poll = models.ForeignKey(Poll, blank=False, null=False, on_delete=models.CASCADE, related_name='poll_votes_count')
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.party.name

class SurveyCategory(models.Model):
    surveyName = models.CharField(max_length=60)

    def __str__(self):
        return self.surveyName

class SurveyResponse(models.Model):
    surveyCategory = models.ForeignKey(SurveyCategory, blank=False, null=False, on_delete=models.CASCADE, related_name="survey_category")
    poll = models.ForeignKey(Poll, blank=False, null=False, on_delete=models.CASCADE, related_name="poll_survey")
    voter = models.ForeignKey(Voter, blank=False, null=False, on_delete=models.CASCADE, related_name='voter_survey')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.voter.phone
