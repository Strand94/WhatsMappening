from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=150)
    ingress = models.CharField(max_length=300, blank=True, default='')
    description = models.CharField(max_length=3000, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now())
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    coordinates = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='events', blank=True)


class Participation(models.Model):
    going = 'G'
    interested = 'I'
    type_choices = (
        (going, 'Going'),
        (interested, 'Interested')
            )

    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance = models.ForeignKey('Attendance', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=type_choices, default=going)

    class Meta:
        unique_together = ('user', 'attendance')
        ordering = ['timestamp']


class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    participants = models.ManyToManyField(User, blank=True, through=Participation)
