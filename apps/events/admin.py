from django.contrib import admin

from .models import *


class ParticipationInline(admin.TabularInline):
    model = Participation


class AttendanceAdmin(admin.ModelAdmin):
    model = Attendance
    filter_horizontal = ('participants',)
    inlines = [
        ParticipationInline,
    ]


class AttendanceInline(admin.StackedInline):
    model = Attendance
    filter_horizontal = ('participants',)
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [
        AttendanceInline,
    ]
    exclude = ('timestamp','author')


admin.site.register(Event, EventAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Category)