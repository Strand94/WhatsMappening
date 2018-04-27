from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.gis.db import models as geomodels


class Category(models.Model):
    title = models.CharField(max_length=70)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=150)
    ingress = models.CharField(max_length=300, blank=True, default='')
    description = models.CharField(max_length=3000, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = geomodels.PointField(srid=4326, null=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='events', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Starred(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Event, related_name='favorited_by', blank=True)

    def __str__(self):
        return self.user.username

def get_starred(user):
    user_starred = Starred.objects.filter(user=user).first()
    if user_starred:
        return user_starred