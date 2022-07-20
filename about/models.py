from django.db import models
from django.utils import timezone


class Aboutmyself(models.Model):
    browser = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    datetimenow = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
