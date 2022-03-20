from django.db import models

class Band(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)