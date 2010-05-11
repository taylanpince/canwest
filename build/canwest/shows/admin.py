from django.contrib import admin

from shows.models import Show


class ShowAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("title", "slug", "blurb", "description")
    save_on_top = True
    prepopulated_fields = {
        "slug": ("title", )
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug"), "blurb", "description", "photo"),
        }),
    )


admin.site.register(Show, ShowAdmin)
