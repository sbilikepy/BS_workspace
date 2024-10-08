from django.contrib.auth.models import AbstractUser
from django.db import models


# https://pyrewood-village.eu/


class User(AbstractUser):
    """Guild owner, who manage recruiting part
    -- also main User"""

    class Meta:
        verbose_name_plural = "Users"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}"


class InGameClass(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Classes"
        ordering = ["name"]

    def __str__(self):
        return self.name


class InGameSpec(models.Model):
    name = models.CharField(
        max_length=255, unique=True
    )  # TODO: check for Frost Holy  Protection

    class Meta:
        verbose_name_plural = "Specialisations"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Character(models.Model):
    class_name = models.ForeignKey(
        InGameClass, on_delete=models.CASCADE, related_name="character_class"
    )
    spec_name = models.ForeignKey(
        InGameSpec, on_delete=models.CASCADE, related_name="character_spec"
    )

    class Meta:
        verbose_name_plural = "Characters"
        constraints = [
            models.UniqueConstraint(
                fields=["class_name", "spec_name"], name="unique_class_spec"
            ),
        ]
        ordering = ["spec_name"]

    def get_class_image(self):
        if self.class_name.name == "Death Knight":
            return "character_icons/spec_icons/death_knight/dk.jpeg"
        return f"character_icons/spec_icons/{self.class_name}/{self.class_name}.jpeg"

    def get_spec_image(self):
        if self.class_name.name == "Death Knight":
            return f"character_icons/spec_icons/death_knight/{self.spec_name.name}.jpg"
        if self.spec_name.name == "Feral DPS":
            return "character_icons/spec_icons/druid/Feral_cat.jpg"
        if self.spec_name.name == "Feral Tank":
            return "character_icons/spec_icons/druid/Feral_bear.jpg"
        if self.spec_name.name == "Beast Mastery":
            return "character_icons/spec_icons/hunter/Beast_Mastery.jpg"

        if self.spec_name.name == "Protection":
            if self.class_name.name == "Warrior":
                return "character_icons/spec_icons/warrior/Protection.jpg"
            return "character_icons/spec_icons/paladin/Protection.jpg"

        if self.spec_name.name == "Holy":
            if self.class_name.name == "Paladin":
                return "character_icons/spec_icons/paladin/Holy.jpg"
            return "character_icons/spec_icons/priest/Holy.jpg"

        return f"character_icons/spec_icons/{self.class_name.name}/{self.spec_name.name}.jpg"

    def __str__(self):
        return f"{self.spec_name} {self.class_name}"


class Recruit(models.Model):
    UPTIME_DAYS_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]
    nickname = models.CharField(max_length=255, blank=False, null=False, unique=True)
    character = models.ForeignKey(Character, on_delete=models.SET_DEFAULT, default=None)
    note = models.CharField(max_length=255, blank=True, null=True)
    wcl = models.IntegerField(blank=True, null=True)  # TODO: WCL API sync
    uptime_days = (
        models.CharField(  # TODO: make it as foreign key to PlannedActivity or smth
            max_length=255, choices=UPTIME_DAYS_CHOICES, null=True, blank=True
        )
    )
    rt_start = models.TimeField(default=None, null=True, blank=True)
    rt_end = models.TimeField(default=None, null=True, blank=True)
    discord_tag = models.CharField(
        max_length=255, null=False, blank=True, default="unknown"
    )

    class Meta:
        verbose_name_plural = "Recruits"
        ordering = ["nickname"]

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

    class Meta:
        verbose_name_plural = "Planned activities"
        ordering = ["by_team"]

    def __str__(self):
        return f"{self.raid_day}: {self.start_time} -> {self.end_time}"


class Team(models.Model):
    guild = models.ForeignKey(
        "Guild", on_delete=models.CASCADE, blank=False, null=False
    )
    team_name = models.CharField(
        max_length=255, default=guild.name, null=True, blank=True
    )

    team_size = models.IntegerField()
    team_progress = models.IntegerField(default=0)
    active_search = models.BooleanField(default=True)
    looking_for = models.ManyToManyField(
        Character, related_name="looking_for", blank=True, default=None
    )
    team_note = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
    )

    required_active_days_amount = models.IntegerField(default=0)

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

    class Meta:
        verbose_name_plural = "Teams"
        ordering = ["?"]
        constraints = [
            models.UniqueConstraint(
                fields=["team_name", "guild"], name="unique_team_guild"
            ),
        ]

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

    class Meta:
        verbose_name_plural = "Guilds"
        ordering = ["?"]

    def __str__(self):
        return f"{self.name}"
