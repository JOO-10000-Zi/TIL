from django.db import models

# Create your models here.
class reviews(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)
    