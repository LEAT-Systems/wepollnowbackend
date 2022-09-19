from django.db import models

# Create your models here.
class States(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.IntegerField()

    def __str__(self):
        return self.name

class Senatorial(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Lga(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    state_id = models.ForeignKey(States, on_delete=models.CASCADE)
    senatorial_id = models.ForeignKey(Senatorial, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
