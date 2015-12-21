from django.contrib import admin

from redinstagram.models import Hashtag


@admin.register(Hashtag)
class HashtagModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    inlines = (
    )

    search_fields = (
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
