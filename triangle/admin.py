from django.contrib import admin

from .models import Person


# Home task 7. Model Person
# admin.site.register(Person)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]
