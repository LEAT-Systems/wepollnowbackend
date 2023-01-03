from django.db import models

from poll.models import Poll, PollCategory

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name

class Senatorial(models.Model):
    name = models.CharField(max_length=40)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Constituency(models.Model):
    name = models.CharField(max_length=40)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lga(models.Model):
    name = models.CharField(max_length=40)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    senatorial_id = models.ForeignKey(Senatorial, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Party(models.Model):
    name = models.CharField(max_length=40)
    abbr = models.CharField( blank=True, null=True, max_length=8)
    logo = models.ImageField(default='Account-user.png', upload_to='party_pictures')
   
    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=40)
    poll = models.ForeignKey(Poll, blank=True,  null=True, on_delete=models.SET_NULL, related_name="poll_candidate")
    poll_category = models.ForeignKey(PollCategory, blank=False,  null=True, on_delete=models.SET_NULL, related_name="pollCategory_candidate")
    party = models.ForeignKey(Party, blank=False, null=True, on_delete=models.SET_NULL, related_name="party_candidate")
    state_id = models.ForeignKey(State, blank=True,  null=True, on_delete=models.SET_NULL, related_name="state_candidate")
    senatorial_id = models.ForeignKey(Senatorial, blank=True,  null=True, on_delete=models.SET_NULL, related_name="senatorial_candidate")
    constituency_id = models.ForeignKey(Constituency, on_delete=models.CASCADE, related_name="constituency_candidate")
    main_candidate = models.BooleanField(default=True)
    candidate_picture = models.ImageField(upload_to="candidate_pics", default="Account-user.png")
    
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=300)
    email = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email = models.CharField(max_length=40)
    
    def __str__(self):
        return self.email