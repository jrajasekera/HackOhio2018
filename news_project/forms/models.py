from django.db import models

class Source(models.Model):
 displayName = models.CharField(max_length=30, primary_key=True)   
 srcName = models.CharField(max_length=30)
