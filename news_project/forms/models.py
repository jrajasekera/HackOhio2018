from django.db import models

class Source(models.Model): 
    displayName = models.CharField(max_length=30, primary_key=True)   
    srcName = models.CharField(max_length=30)
    partisanBias = models.IntegerField()
    factualAccuracy = models.IntegerField()

class SortBy(models.Model):
    displaySortBy = models.CharField(max_length=30, primary_key=True)
    apiSortBy = models.CharField(max_length=30)

class Category(models.Model):
    displayCat = models.CharField(max_length=30, primary_key=True)
    apiCat = models.CharField(max_length=30)

class Language(models.Model):
    displayLang = models.CharField(max_length=30, primary_key=True)
    apiLang = models.CharField(max_length=30)

class Country(models.Model):
    displayctry = models.CharField(max_length=85, primary_key=True)
    apiCtry = models.CharField(max_length=85)

class SearchHistory(models.Model):
    id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=30)
    sortBy = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
