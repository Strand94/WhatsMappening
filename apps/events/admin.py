from django.contrib import admin
from . models import *
from leaflet.admin import LeafletGeoAdmin


class EventAdmin(LeafletGeoAdmin):
    list_display = ('title', 'location')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'name')


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')


# Register your models here.
admin.site.register(Event, LeafletGeoAdmin)
admin.site.register(Category, CategoryAdmin)
