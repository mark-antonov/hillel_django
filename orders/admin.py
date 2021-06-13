from django.contrib import admin

from .models import City, Client, Product, Supplier


# HT 8. OneToOneField, ForeignKey, ManyToManyField
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "date_created"]
    date_hierarchy = "date_created"  # date filter widget


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "id", "city"]
    filter_horizontal = ["product"]  # many-to-many relationship widget


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "city"]
