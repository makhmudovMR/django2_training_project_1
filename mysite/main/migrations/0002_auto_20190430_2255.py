# Generated by Django 2.2 on 2019-04-30 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 30, 22, 55, 44, 407367)),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_slug',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_slug',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
