from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from .forms import EventForm
from .models import Event, SimpleEvent, Attendance, Participation, Category
from django.utils import timezone
from django.shortcuts import redirect
import json


def interface(request):
    return render(request, 'events/eventInterface.html')


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.timestamp = timezone.now()
            event.save()
            return redirect('events:interface')
    form = EventForm(request.POST)
    return render(request, 'events/eventForm.html', {'form': form})


def testDjango(request):
    return render(request, 'events/testGeoDjango.html')


def showEvents(request):
    points = serialize('geojson', Event.objects.all())
    return HttpResponse(points, content_type='json')


def showCategories(request):
    categories = serialize('json', Category.objects.all())
    return HttpResponse(categories, content_type='json')


def showRequestedEvents(request, values):
    liste = json.loads(values)
    value = []
    for item in liste:
        value.append(int(item))
    events = serialize('geojson', Event.objects.filter(category_id__in = value))
    return HttpResponse(events, content_type='json')
