from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ('created_at',)
    list_editable = ('new_building',)
    list_display = ('town', 'address','price', 'construction_year', 'new_building')
admin.site.register(Flat, FlatAdmin)
