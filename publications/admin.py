from django.contrib import admin

from .models import Publication, Review


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    """Админ панель по постам. Поля для отображения: title, author, created_at. Поле для фильтра: author, created_at.
    Поле для поиска: title."""

    list_display = ("title", "author", "created_at")
    list_filter = ("author", "created_at")
    search_fields = ("title",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Админ панель по отзывам. Поля для отображения: text, author, created_at. Поле для фильтра: author, created_at.
    Поле для поиска: text."""

    list_display = ("text", "author", "created_at")
    list_filter = ("author", "created_at")
    search_fields = ("text",)
