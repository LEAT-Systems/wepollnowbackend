from django.db import models

# Create your models here.
class States(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.IntegerField(max_length=30)

    def __str__(self):
        return self.name


class Lga(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    state_id = models.IntegerField(rel=States.id)