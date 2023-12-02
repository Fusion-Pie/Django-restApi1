from django.db import models

# Create your models here.
class GangInfo(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    collegeName = models.CharField(max_length = 200)
    # auto_now_add will set the time when the instance is created
    createdAt = models.DateField(auto_now_add = True)
    # auto_add will set the time when the instance is modified
    modifiedAt = models.DateField(auto_now = True)