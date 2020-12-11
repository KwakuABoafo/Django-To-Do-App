from django.db import models

# Create your models here.
class Item(models.Model):
    task = models.CharField(max_length=100)
    isComplete = models.BooleanField()

    def __str__(self):
        return self.task