from django.contrib import admin

from .models import Author, Quote


# HT 13. Celery beat
class QuoteInlineModelAdmin(admin.TabularInline):
    """Defines format of inline quotes insertion (used in AuthorAdmin)"""
    model = Quote
    extra = 3


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'born_date', 'born_location', 'description']
    fields = ['name', ('born_date', 'born_location'), 'description']
    search_fields = ['name']
    inlines = [QuoteInlineModelAdmin]
    list_per_page = 10


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'author']
    list_filter = ['author']
    list_per_page = 10
