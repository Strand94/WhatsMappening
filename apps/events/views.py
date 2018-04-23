from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from .forms import EventForm
from .models import Event, Attendance, Participation, Category
from django.utils import timezone
from django.shortcuts import redirect
import json


def create_event(request):
    action = 'Create new'
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.timestamp = timezone.now()
            event.start = str(request.POST.get(("startDate"), "")+" "+request.POST.get(("startTime"), ""))
            event.end = str(request.POST.get(("endDate"), "")+" "+request.POST.get(("endTime"), ""))
            event.save()
            attendance = Attendance.objects.create(event=event)
            participation = Participation.objects.create(attendance=attendance, user=request.user, status='G')
            attendance.save()
            participation.save()
            return redirect('events:user_events')
    form = EventForm(request.POST)
    return render(request, 'events/eventForm.html', {
        'form':form,
        'action':action
    })


def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    start_dateTime = str(event.start).split()
    end_dateTime = str(event.end).split()
    start_date = (start_dateTime[0])
    start_time = (start_dateTime[1][0:8])
    end_date = (end_dateTime[0])
    end_time = (end_dateTime[1][0:8])
    owner = event.author
    action = 'Edit'
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        print("load form")
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.timestamp = timezone.now()
            event.start = str(request.POST.get(("startDate"), "") + " " + request.POST.get(("startTime"), ""))
            event.end = str(request.POST.get(("endDate"), "") + " " + request.POST.get(("endTime"), ""))
            event.save()
            return redirect('events:event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event, initial={'startDate': start_date, 'startTime': start_time, 'endDate': end_date, 'endTime': end_time})
    return render(request, 'events/eventForm.html',{
        'form':form,
        'action':action,
        'owner':owner,
    })


def user_created(request):
    events = Event.objects.filter(author=request.user)
    return render(request, 'events/userCreated.html',{
        'events':events,
    })


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/eventDetail.html', {'event':event})
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
