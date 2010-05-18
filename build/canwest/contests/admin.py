from django.contrib import admin

from contests.models import Contest, Sponsor


class SponsorAdmin(admin.StackedInline):
    model = Sponsor


class ContestAdmin(admin.ModelAdmin):
    list_display = ("title", )
    inlines = [
        SponsorAdmin,
    ]

    search_fields = ("title", "slug", "description")
    save_on_top = True
    prepopulated_fields = {
        "slug": ("title", )
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug"), "description", "header"),
        }),
    )


admin.site.register(Contest, ContestAdmin)
