from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django.utils.html import format_html

from .models import HomePage, HomePageImage, ServicesPage, AboutPage, Quote


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
        ("En-tête", {"fields": ("title", "subtitle")}),
        ("Contenu principal", {"fields": ("body",)}),
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
    fieldsets = (("À propos", {"fields": ("title", "body", "image")}),)
    list_display = ("__str__",)
    search_fields = ("title",)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("short_text", "author", "created_at")
    search_fields = ("text", "author")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("text", "author")}),
        ("Horodatage", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    @admin.display(description="Texte")
    def short_text(self, obj):
        return obj.text[:80] + "\u2026" if len(obj.text) > 80 else obj.text
