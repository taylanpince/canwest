from django.contrib import admin

from shows.models import Show, ShowCategory


class ShowAdmin(admin.ModelAdmin):
    list_display = ("title", "category", )
    list_filter = ("category", )
    search_fields = ("title", "slug", "blurb", "description")
    save_on_top = True
    prepopulated_fields = {
        "slug": ("title", )
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug"), "category", "blurb", "description", "logo", "photo"),
        }),
    )


class ShowCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "global_template")
    list_filter = ("global_template", )
    search_fields = ("title", "slug")
    save_on_top = True
    prepopulated_fields = {
        "slug": ("title", )
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug"), "global_template"),
        }),
    )


admin.site.register(Show, ShowAdmin)
admin.site.register(ShowCategory, ShowCategoryAdmin)
