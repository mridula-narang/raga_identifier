from django.db import models
from django.conf import settings

# Create your models here.
class Audio(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audio/')
    uploaded_date = models.DateTimeField()
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    