# Generated by Django 3.2.8 on 2023-08-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_listing_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
