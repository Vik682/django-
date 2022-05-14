from django.db import models
from authentication.models import User

# Create your models here.
class Student(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=30, default='')
  entry_no = models.CharField(max_length=30)
  programme = models.CharField(max_length=30)
  branch = models.CharField(max_length=30)
  phone_number = models.CharField(max_length=20)
  address = models.CharField(max_length=100)
