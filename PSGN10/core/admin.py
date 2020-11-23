from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# from libs.admin_register import AdminRegister
from .models import AwayStats, HomeStats, Player


@admin.register(AwayStats)
class AwayStatsAdmin(admin.ModelAdmin):
    pass


@admin.register(HomeStats)
class HomeStatsAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
