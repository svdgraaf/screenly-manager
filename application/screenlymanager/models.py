from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    last_ip = models.IPAddressField(blank=True)
    last_active = models.DateTimeField(blank=True)
    notes = models.TextField(max_length=1024)
