# Generated by Django 3.2.5 on 2021-07-20 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auto_20210719_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='watching',
        ),
    ]
