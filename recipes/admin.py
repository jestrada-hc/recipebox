from django.contrib import admin
from .models import Category, Tag, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "difficulty", "total_minutes", "created_at")
    list_filter = ("category", "difficulty", "tags")
    search_fields = ("title", "description", "ingredients")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
