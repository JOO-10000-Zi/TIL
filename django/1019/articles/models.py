
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
# class Article(models.Model):
#     user = models.ForeignKey(on_delete=models.CASCADE)
#     title = models.CharField(max_length=80)
#     content = models.TextField()
#     image = ProcessedImageField(upload_to='articles/',blank=True,
#                                 processors=[ResizeToFill(400,300)],
#                                 format='JPEG',
#                                 options={'quality' : 80 })