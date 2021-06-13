# Generated by Django 3.2.3 on 2021-05-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_auto_20210528_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]