from django.db import models

class regddata(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    mobile=models.BigIntegerField()
