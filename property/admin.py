from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    readonly_fields = ('created_at',)
    list_editable = ('new_building',)
    list_display = ('town', 'address','price', 'construction_year', 'new_building')
    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
