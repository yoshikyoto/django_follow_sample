from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    follow_users = models.ManyToManyField("User", related_name="follower_users")
