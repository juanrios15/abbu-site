from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django.utils.html import format_html

from .models import HomePage, HomePageImage, ServicesPage, AboutPage


class HomePageImageInline(admin.TabularInline):
    model = HomePageImage
    extra = 1
    fields = ("preview", "image", "caption", "order")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj and obj.image:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;" />', obj.image.url)
        return "—"


@admin.register(HomePage)
class HomePageAdmin(SingletonModelAdmin):
    inlines = [HomePageImageInline]
    fieldsets = (
        ("Header", {"fields": ("title", "subtitle")}),
        ("Main content", {"fields": ("body",)}),
    )
    list_display = ("__str__",)
    search_fields = ("title", "subtitle")


@admin.register(ServicesPage)
class ServicesPageAdmin(SingletonModelAdmin):
    fieldsets = (
        ("Section 1", {"fields": ("section1_title", "section1_body")}),
        ("Section 2", {"fields": ("section2_title", "section2_body")}),
    )
    list_display = ("__str__",)
    search_fields = ("section1_title", "section2_title")


@admin.register(AboutPage)
class AboutPageAdmin(SingletonModelAdmin):
    fieldsets = (("About the studio", {"fields": ("title", "body", "image")}),)
    list_display = ("__str__",)
    search_fields = ("title",)
