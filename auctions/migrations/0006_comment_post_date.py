# Generated by Django 3.2.5 on 2021-07-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_rename_imgage_auctionlisting_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_date',
            field=models.DateField(auto_now=True),
        ),
    ]
