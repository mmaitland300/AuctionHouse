# Generated by Django 3.2.5 on 2021-07-19 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_remove_user_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watching',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='auctions.auctionlisting'),
        ),
    ]
