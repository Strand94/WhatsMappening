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

class StarredAdmin(admin.ModelAdmin):
       filter_horizontal = ('favorites',)


# Register your models here.
admin.site.register(Event, LeafletGeoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Starred, StarredAdmin)
