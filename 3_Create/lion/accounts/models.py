from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    major = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
