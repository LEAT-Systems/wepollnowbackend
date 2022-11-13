from django.db import models
from utilities.models import *
from voters.models import *
from django.utils import timezone
from django.core.exceptions import ValidationError


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
    poll_date = models.DateTimeField(auto_now_add='True')
    poll_state = models.IntegerField()
    poll_senatorial_district = models.IntegerField()
    poll_lga = models.IntegerField()
    poll_startDate = models.DateTimeField(default=timezone.now)
    poll_endDate = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.poll_category.title
    
    def clean(self):
        super().clean()
        if not (timezone.now() <= self.poll_startDate <= self.poll_endDate):
            raise ValidationError('End date has to be greater than start date')
