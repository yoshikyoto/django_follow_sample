# Generated by Django 3.1.5 on 2021-01-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0002_user_follow_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follow_users',
            field=models.ManyToManyField(related_name='follower_users', to='follow_app.User'),
        ),
    ]
