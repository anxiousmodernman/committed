from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class AccessToken(models.Model):
    token = models.TextField(max_length=200)
    user = models.ForeignKey(User)

