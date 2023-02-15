from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'currency']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']
    list_filter = ['price', 'currency', 'name']
    ordering = ['-id']


admin.site.register(Item, ItemAdmin)
