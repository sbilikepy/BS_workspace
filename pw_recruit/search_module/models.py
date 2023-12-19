from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models


# https://pyrewood-village.eu/


class User(AbstractUser):
    """Guid owner, who manage recruiting part"""

    guild = models.ForeignKey(
        "Guild",
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="users_guild",
    )


class InGameClass(models.Model):
    name = models.CharField(max_length=255, unique=True)


class InGameSpec(models.Model):
    name = models.CharField(max_length=255, unique= True) #TODO: check for Frost Holy  Protection


class Character(models.Model):
    class_name = models.ForeignKey(
        InGameClass, on_delete=models.CASCADE, related_name="character_class"
    )
    spec_name = models.ForeignKey(
        InGameSpec, on_delete=models.CASCADE, related_name="character_spec"
    )


class Recruit(models.Model):
    nickname = models.CharField(max_length=255, blank=False, null=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    note = models.CharField(max_length=255, blank=True, null=True)
    wcl = models.IntegerField(
        blank=True, null=True
    )  # TODO: WCL API sync


class Team(models.Model):
    guild = models.ForeignKey("Guild", on_delete=models.CASCADE)
    team_name = models.CharField(max_length=255)
    team_size = models.IntegerField()
    team_progress = models.IntegerField(default=0)
    active_search = models.BooleanField(default=True)
    looking_for = models.ManyToManyField(Character, related_name="looking_for")


class Guild(models.Model):
    """Main list object"""

    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="guild_owner",
        blank=False,
        null=False,
    )
    highest_progress = models.CharField(
        max_length=5
    )  # TODO: set to max(Guild.team.team_progress)
    teams = models.ForeignKey(
        Team,
        default=None,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="guid_teams",
    )
