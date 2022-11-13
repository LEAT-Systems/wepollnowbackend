from django.db import models

from poll.models import Poll

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

class Lga(models.Model):
    name = models.CharField(max_length=40)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    senatorial_id = models.ForeignKey(Senatorial, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Party(models.Model):
    name = models.CharField(max_length=40)

    
    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=40)
    poll = models.ForeignKey(Poll, blank=False,  null=True, on_delete=models.SET_NULL)
    party = models.ForeignKey(Party, blank=False, on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    main_candidate = models.BooleanField(default=False)
    candidate_picture = models.ImageField(upload_to="candidate_pics", default="Account-user.png")
    
    def __str__(self):
        return self.name

class Subscriber(models.Model):
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=300)
    email = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name