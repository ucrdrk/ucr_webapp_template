from django.contrib import admin
from .models import Games

class GamesAdmin(admin.ModelAdmin):
    list_display = ("game_name","game_year",)


admin.site.register(Games,GamesAdmin)