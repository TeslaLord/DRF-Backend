# Generated by Django 3.1.7 on 2021-03-15 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_bookingtime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingtime',
            old_name='advisort',
            new_name='advisor',
        ),
    ]
