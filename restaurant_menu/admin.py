from django.contrib import admin
from .models import Item, Info

# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")

class InfoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "date_created")
    search_fields = ("title", "description")



admin.site.register(Item, MenuItemAdmin)
admin.site.register(Info, InfoAdmin)