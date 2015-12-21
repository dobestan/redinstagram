from django.contrib import admin

from instagram.models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'hashtag',
    )

    inlines = (
    )

    search_fields = (
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
