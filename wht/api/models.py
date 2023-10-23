from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Team {self.name}'


class Member(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

    def __str__(self):
        return f'id: {self.id}, username: {self.username}'
