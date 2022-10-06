from django.db import models

# Create your models here.
class reviews(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    running_time = models.IntegerField()
    