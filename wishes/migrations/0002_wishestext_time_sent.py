# Generated by Django 4.0.6 on 2022-07-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishestext',
            name='time_sent',
            field=models.IntegerField(default=0),
        ),
    ]
