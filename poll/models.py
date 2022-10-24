from django.db import models
from utilities.models import *
from voters.models import *
from django.utils import timezone


# Create your models here.
class PollCategory(models.Model):
    title = models.CharField(max_length=30)
    poll_description = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add='True')
    updated_date = models.DateTimeField(auto_now='True')


    def __str__(self):
        return self.title


class Poll(models.Model):
    poll_category = models.ForeignKey(PollCategory, blank=False, on_delete=models.CASCADE)
    poll_date = models.DateTimeField(editable=False)
    poll_state = models.ForeignKey(States,blank=True, null=True, on_delete=models.CASCADE)
    poll_senatorial_district = models.ForeignKey(Senatorial, blank=True, null=True,  on_delete=models.CASCADE)
    poll_lga = models.ForeignKey(Lga,blank=True, null=True,  on_delete=models.CASCADE)

class PollOption(models.Model):
    poll_question_id = models.ForeignKey(PollCategory, blank=False, on_delete=models.CASCADE, related_name='categories')
    option_title = models.CharField(max_length=50)
    option_image = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add='True')
    updated_date = models.DateTimeField(auto_now='True')

    def __str__(self):
        return self.option_title

class PollResult(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    poll_option = models.ForeignKey(PollOption, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    vote_date = models.DateTimeField(auto_now_add='True')