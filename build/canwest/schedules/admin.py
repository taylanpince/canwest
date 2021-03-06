from django.contrib import admin

from schedules.models import ScheduledItem


class ScheduledItemAdmin(admin.ModelAdmin):
    list_display = ("title", "start_time", "day",)
    list_filter = ("day",)
    search_fields = ("title",)
    save_on_top = True


admin.site.register(ScheduledItem, ScheduledItemAdmin)
