# Generated by Django 3.2.5 on 2021-07-19 21:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210719_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 19, 21, 45, 23, 300101)),
        ),
    ]