# Generated by Django 3.1.1 on 2021-02-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='offer',
            field=models.BooleanField(default=False, verbose_name='Offer'),
        ),
    ]
