from django.db import models
import requests

# Create your models here.
class character(models.Model):
    charname = models.CharField(max_length=40, default="", help_text="Your name")
    hp = models.IntegerField(default=1, help_text="Hit Points")
    ac = models.IntegerField(default=10, help_text="Armor Class")