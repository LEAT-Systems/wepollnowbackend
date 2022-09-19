from django.db import models
from utilities.models import *
from voters.models import *

# Create your models here.
class Poll(models.Model):
    poll_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    poll_date = models.DateTimeField(auto_now=True)
    poll_description = models.TextField(max_length=200)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle


class Poll_Category(models.Model):
    poll_category_id = models.IntegerField(primary_key=True)
    poll_id = models.ForeignKey(Poll, blank=False, on_delete=models.CASCADE)
    poll_state = models.ForeignKey(States,default= None, on_delete=models.CASCADE)
    poll_senatorial_district = models.ForeignKey(Senatorial, default= None, on_delete=models.CASCADE)
    poll_lga = models.ForeignKey(Lga, default= None, on_delete=models.CASCADE)

class Poll_Option(models.Model):
    poll_option_id = models.IntegerField(primary_key=True)
    poll_question_id = models.ForeignKey(Poll_Category, blank=False, on_delete=models.CASCADE)
    option_title = models.CharField(max_length=50)
    option_image = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.option_title

class Poll_Result(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    poll_question_id = models.ForeignKey(Poll_Category, on_delete=models.CASCADE)
    poll_option = models.ForeignKey(Poll_Option, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)