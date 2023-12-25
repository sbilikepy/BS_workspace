from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from search_module.models import *


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
        "is_staff",
        "is_active",
        "date_joined"
    ]


@admin.register(InGameClass)
class InGameClassAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(InGameSpec)
class InGameSpecAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["class_name", "spec_name"]


@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    list_display = ["nickname", "character", "note", "wcl", "uptime_days", "rt_start", "rt_end"]


@admin.register(PlannedActivity)
class PlannedActivityAdmin(admin.ModelAdmin):
    list_display = ["raid_day", "start_time", "end_time", "by_team"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["team_name", "guild", "team_size", "loot_system", "team_progress",
                    "active_search", "team_note",
                    "required_active_days_amount"]


@admin.register(Guild)
class GuildAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner",
        "faction",
        "highest_progress",
        "discord_link",
        "apply_link",
    ]
