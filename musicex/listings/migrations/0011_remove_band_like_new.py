# Generated by Django 3.2.8 on 2023-08-28 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]