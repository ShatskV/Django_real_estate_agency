from django.contrib import admin

from .models import Complaint, Flat, Owner


class OwnersInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    readonly_fields = ('created_at',)
    list_editable = ('new_building',)
    list_display = ('town', 'address','price', 'construction_year', 'new_building')
    raw_id_fields = ('liked_by', 'owned_by')
    inlines = [OwnersInline, ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
