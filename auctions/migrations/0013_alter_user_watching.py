# Generated by Django 3.2.5 on 2021-07-19 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_user_watching'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watching',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='auctions.auctionlisting'),
        ),
    ]
