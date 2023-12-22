from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from search_module.models import *


@admin.register(InGameClass)
class InGameClassAdmin(admin.ModelAdmin):
    pass


@admin.register(InGameSpec)
class InGameSpecAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    pass


@admin.register(PlannedActivity)
class PlannedActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Guild)
class GuildAdmin(admin.ModelAdmin):
    pass
