from django.db import models

class Randomstr(models.Model):
    
    length = models.CharField(max_length=100)
    digits = models.BooleanField(default=False)
    specials = models.BooleanField(default=False)
