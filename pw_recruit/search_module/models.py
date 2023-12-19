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
        on_delete=models.SET_NULL,
        related_name="users_guild",
    )

    def __str__(self):
        if self.guild:
            return f"{self.username} - {self.guild.name} owner"
        else:
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
    uptime = models.ForeignKey(
        "PlannedActivity",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name="recruit_uptime",
    )

    def __str__(self):
        return f"{self.nickname}: Character: {self.character}. Note: {self.note}. WCL: {self.wcl}. Uptime: {self.uptime}"


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
        "Team", on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self):
        return f"{self.raid_day}: {self.start_time} -> {self.end_time}"


class Team(models.Model):
    team_name = models.CharField(max_length=255)
    team_size = models.IntegerField()
    team_progress = models.IntegerField(default=0)
    active_search = models.BooleanField(default=True)
    looking_for = models.ManyToManyField(Character, related_name="looking_for")
    team_note = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
    )
    activities = models.ManyToManyField(PlannedActivity, related_name="activities")

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

    def __str__(self):
        return f"Team {self.team_name}"


class Guild(models.Model):
    """Main list object"""

    FACTION_CHOICES = [
        ("Alliance", "Alliance"),
        ("Horde", "Horde"),
    ]
    name = models.CharField(max_length=255, blank=False, null=False)
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
    highest_progress = models.CharField(
        max_length=5
    )  # TODO: set to max(Guild.team.team_progress)
    teams = models.ManyToManyField(
        Team,
        blank=True,
        null=True,
        related_name="teams",
    )
    discord_link = models.CharField(max_length=255, null=True, blank=True)
    apply_link = models.CharField(max_length=255, null=True, blank=True)
    wcl_link = models.URLField(verbose_name="wcl_link", null=True, blank=True)
    guild_note = models.CharField(max_length=1000, null=True, blank=True)
    avatar = models.CharField(
        max_length=255, null=True, blank=True
    )  # link to img TODO: read comment below

    # avatar = models.ImageField(upload_to='guild_avatars/', null=True, blank=True)
    # +
    # settings.py
    # MEDIA_URL = '/media/'
    # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    def __str__(self):
        return f"{self.name}"

        # return (
        #     f"{self.name}. Faction: {self.faction}. GM/recruiter: {self.owner}. Teams: {teams_str}. Discord: {self.discord_link}. "
        #     f"Apply link: {self.apply_link}. WCL link: {self.wcl_link}. Note: {self.guild_note}"
        # )
