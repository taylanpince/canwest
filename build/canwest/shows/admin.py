from django.contrib import admin

from shows.models import Show, Channel, ShowCategory


class ShowAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order")
    list_filter = ("category", )
    search_fields = ("title", "slug", "blurb", "description")
    save_on_top = True
    prepopulated_fields = {
        "slug": ("title", )
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug", "order"), ("category", "channel"), "blurb", "description", "logo", "photo"),
        }),
    )


class ChannelAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order")
    list_filter = ("category", )
    search_fields = ("title", "slug")
    save_on_top = True
    prepopulated_fields = {
        "slug": ("title", )
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug", "order"), "category", "logo"),
        }),
    )


class ShowCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "global_template")
    list_filter = ("global_template", )
    search_fields = ("title", "slug")
    save_on_top = True
    prepopulated_fields = {
        "slug": ("title", )
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug", "order"), "global_template"),
        }),
    )


admin.site.register(Show, ShowAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(ShowCategory, ShowCategoryAdmin)
