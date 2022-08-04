
from django.db import models

class Booktmodel (models.Model):
    id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    writer=models.CharField(max_length=100)
    publication=models.CharField(max_length=150)
    status=models.CharField(max_length=20,default="AVAILABLE")
