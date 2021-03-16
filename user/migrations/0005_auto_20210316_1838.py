# Generated by Django 3.1.7 on 2021-03-16 18:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_auto_20210315_0601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingtime',
            name='advisor',
        ),
        migrations.AddField(
            model_name='bookingtime',
            name='advisor',
            field=models.ManyToManyField(to='user.Advisor'),
        ),
        migrations.RemoveField(
            model_name='bookingtime',
            name='user',
        ),
        migrations.AddField(
            model_name='bookingtime',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
