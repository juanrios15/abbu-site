from django.contrib import admin
from django.utils.html import format_html

from .models import Project, ProjectImage, ProjectBeforeImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("preview", "image", "caption", "order")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj and obj.image:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;" />', obj.image.url)
        return "—"


class ProjectBeforeImageInline(admin.TabularInline):
    model = ProjectBeforeImage
    extra = 1
    fields = ("preview", "image", "caption", "order")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj and obj.image:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;" />', obj.image.url)
        return "—"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title", "subtitle", "summary")
    inlines = [ProjectImageInline, ProjectBeforeImageInline]
    fieldsets = (
        ("Main", {"fields": ("title", "subtitle", "summary", "content")}),
        ("Before (Avant)", {"fields": ("before_text",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
    readonly_fields = ("slug", "created_at", "updated_at")
