# Generated by Django 3.2.5 on 2021-07-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_comment_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.BooleanField(default=False),
        ),
    ]
