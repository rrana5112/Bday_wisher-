# Generated by Django 4.0.6 on 2022-07-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('category', models.CharField(choices=[('Parents', 'Parents'), ('Family', 'Family'), ('Siblings', 'Siblings'), ('Friends', 'Friends'), ('Special', 'Special'), ('Colleagues', 'Colleagues')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='WishesText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('Parents', 'Parents'), ('Family', 'Family'), ('Siblings', 'Siblings'), ('Friends', 'Friends'), ('Special', 'Special'), ('Colleagues', 'Colleagues')], max_length=15)),
            ],
        ),
    ]
