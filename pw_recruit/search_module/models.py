from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Guid owner, who manage recruiting part"""
    owner = models.BooleanField()
    guild = models.ForeignKey(
        Guild, default=None, blank=True, on_delete=models.PROTECT, related_name="users_guild"
    )


class Guild(models.Model):
    """Main list object"""
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="guild_owner"
    )
    highest_progress = models.CharField(max_length=5)  # (12/12)
    teams = models.ForeignKey(Team, default=None, blank=True, on_delete=models.PROTECT, related_name="guid_teams")


class Team(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.PROTECT)
    team_name = models.CharField(max_length=255)
    team_size = models.IntegerField()
    team_progress = models.IntegerField()
    lf_players = models.BooleanField()


class GameClass(models.Model):
    class_name = models.CharField(max_length=255)
    class_spec = models.CharField(max_length=255)
