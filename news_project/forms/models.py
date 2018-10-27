from django.db import models

class Source(models.Model):
 displayName = models.CharField(max_length=30, primary_key=True)   
 srcName = models.CharField(max_length=30)

class Sort(models.Model):
 sortBy = models.CharField(max_length=30)

class Category(models.Model):
 catG = models.CharField(max_length=30)

class Language(models.Model):
 lang = models.CharField(max_length=30)

class Country(models.Model):
 ctry = models.CharField(max_length=85)
