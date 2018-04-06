from django.contrib import admin
from . models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'ingress')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'name')


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')


# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Participation, ParticipationAdmin)
admin.site.register(Category, CategoryAdmin)