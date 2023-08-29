from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    name = models.CharField(max_length=100)
    genre = models.CharField(choices=Genre.choices, max_length=5)
    biography = models.CharField(max_length=100)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
   
    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    class Type(models.TextChoices):
        disk = 'Records'
        clothes = 'Clothing'
        poster = 'Posters'
        miscellaneous = 'Miscellaneous'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    sold = models.BooleanField(default=False)
    year_article = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)], null=True, blank=True)
    type = models.CharField(choices=Type.choices, max_length=20)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'

