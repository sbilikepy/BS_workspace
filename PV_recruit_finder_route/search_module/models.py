from django.contrib.auth.models import AbstractUser
from django.db import models


# https://pyrewood-village.eu/


class User(AbstractUser):
    """Guild owner, who manage recruiting part
    -- also main User"""

    pass

    def __str__(self):
        return f"{self.username}"


class InGameClass(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class InGameSpec(models.Model):
    name = models.CharField(
        max_length=255, unique=True
    )  # TODO: check for Frost Holy  Protection

    def __str__(self):
        return self.name


class Character(models.Model):
    class_name = models.ForeignKey(
        InGameClass, on_delete=models.CASCADE, related_name="character_class"
    )
    spec_name = models.ForeignKey(
        InGameSpec, on_delete=models.CASCADE, related_name="character_spec"
    )

    def __str__(self):
        return f"{self.spec_name} {self.class_name}"


class Recruit(models.Model):
    nickname = models.CharField(max_length=255, blank=False, null=False)
    character = models.ForeignKey(Character, on_delete=models.SET_DEFAULT, default=None)
    note = models.CharField(max_length=255, blank=True, null=True)
    wcl = models.IntegerField(blank=True, null=True)  # TODO: WCL API sync
    uptime_days = models.DateField(default=None, null=True, blank=True)
    rt_start = models.TimeField(default=None, null=True, blank=True)
    rt_end = models.TimeField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.nickname}: Character: {self.character}. Note: {self.note}. WCL: {self.wcl}. Uptime: {self.uptime_days}"


class PlannedActivity(models.Model):
    RAID_DAYS_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]
    raid_day = models.CharField(
        max_length=255,
        choices=RAID_DAYS_CHOICES,
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    by_team = models.ForeignKey(
        "Team", on_delete=models.CASCADE, null=False, blank=False, default=None
    )

    def __str__(self):
        return f"{self.raid_day}: {self.start_time} -> {self.end_time}"


class Team(models.Model):
    team_size = models.IntegerField()
    team_progress = models.IntegerField(default=0)
    active_search = models.BooleanField(default=True)
    looking_for = models.ManyToManyField(
        Character, related_name="looking_for", null=True, blank=True, default=None
    )
    team_note = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
    )
    # activities = models.ManyToOneRel(PlannedActivity, related_name="activities")
    required_active_days_amount = models.IntegerField(default=0)

    guild = models.ForeignKey(
        "Guild", on_delete=models.CASCADE, blank=False, null=False
    )
    team_name = models.CharField(
        max_length=255, default=guild.name, null=True, blank=True
    )

    LOOT_SYSTEM_CHOICES = [
        ("Loot Council", "Loot Council"),
        ("EPGP", "EPGP"),
        ("DKP", "DKP"),
        ("SR", "SR"),
        ("BIS > MS > OS roll", "BIS > MS > OS roll"),
        ("GDKP", "GDKP"),
        ("Roll", "Roll"),
        ("Other", "Other"),
    ]

    loot_system = models.CharField(
        max_length=20,
        choices=LOOT_SYSTEM_CHOICES,
        blank=False,
        null=False,
        default="Other",
    )

    def clean(self):
        if not self.team_name:
            self.team_name = self.guild.name
        if self.team_progress > self.guild.highest_progress:
            self.guild.highest_progress = self.team_progress

        self.guild.save()

    def __str__(self):
        return f"Team {self.team_name}"


class Guild(models.Model):
    """Main list object"""

    FACTION_CHOICES = [
        ("Alliance", "Alliance"),
        ("Horde", "Horde"),
    ]
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    faction = models.CharField(
        max_length=10,
        choices=FACTION_CHOICES,
        blank=False,
        null=False,
        default="Unrecognized",
    )
    owner = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="guild_owner",
        blank=False,
        null=False,
    )
    highest_progress = models.IntegerField(
        default=0, null=True, blank=True
    )  # team.clean

    discord_link = models.CharField(max_length=255, null=True, blank=True)
    apply_link = models.CharField(max_length=255, null=True, blank=True)
    wcl_link = models.URLField(verbose_name="wcl_link", null=True, blank=True)
    guild_note = models.CharField(max_length=1000, null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
