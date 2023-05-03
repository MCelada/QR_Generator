from django.db import models

class Wifi(models.Model):
    CONDITION_CHOICES = (
        ('WPA', 'WPA'),
        ('WEP', 'WEP'),
        ('nopass', 'nopass'),
    )
    ssid = models.CharField(max_length=100)
    security = models.CharField(max_length=6, choices = CONDITION_CHOICES)
    password = models.CharField(max_length=100)
