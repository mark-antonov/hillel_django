from django.contrib import admin

from .models import City, Client, Logs, Product, Supplier


# HT 8. OneToOneField, ForeignKey, ManyToManyField
class ClientInlineModelAdmin(admin.TabularInline):
    model = Client


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [ClientInlineModelAdmin]  # allows you to edit related objects on the same page as the parent object.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "date_created"]
    date_hierarchy = "date_created"  # date filter widget
    search_fields = ["name"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "id", "city"]
    list_filter = ["city"]
    filter_horizontal = ["product"]  # many-to-many relationship widget


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "city"]
    list_filter = ["city"]


# HT 9. Middleware, ModelAdmin
@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ["path", "method", "timestamp"]
    list_filter = ["method"]
    date_hierarchy = "timestamp"  # date filter widget
