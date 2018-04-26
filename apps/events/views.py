from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from .forms import EventForm
from .models import Event, Category
from django.utils import timezone
from django.shortcuts import redirect
import datetime
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
    if request.method == 'POST':
        if 'delete_event' in request.POST:
            delete = request.POST.get('delete_event')
            event = Event.objects.filter(pk=delete)
            event.delete()
    return render(request, 'events/userCreated.html',{
        'events':events,
    })


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/eventDetail.html', {'event':event})


def testDjango(request):
    return render(request, 'events/testGeoDjango.html')


def showEvents(request):
    points = serialize('geojson', Event.objects.filter(start__range=[datetime.datetime.now(), (datetime.datetime.now()+datetime.timedelta(days=7))]))
    return HttpResponse(points, content_type='json')


def showTime(request, values):
    date = json.loads(values)
    option = int(date)
    if option == 0:
       points = serialize('geojson', Event.objects.filter(start__range=[datetime.datetime.now(), (datetime.datetime.now() + datetime.timedelta(days=7))]))
    elif option == 1:
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        points = serialize('geojson', Event.objects.filter(start__range=(today_min, today_max)))
    elif option == 2:
        tomorrow_min=datetime.datetime.combine(datetime.date.today()+datetime.timedelta(days=1), datetime.time.min)
        tomorrow_max = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), datetime.time.max)
        points = serialize('geojson', Event.objects.filter(start__range=(tomorrow_min, tomorrow_max)))
    return HttpResponse(points, content_type='json')

def showCustomTime(request, values):
    string =json.loads(values)
    dates=string.split("&&&")
    start_date=datetime.datetime.combine(datetime.datetime.strptime(dates[0], '%Y-%m-%d').date(), datetime.time.min)
    end_date=datetime.datetime.combine(datetime.datetime.strptime(dates[1], '%Y-%m-%d').date(), datetime.time.max)
    points = serialize('geojson', Event.objects.filter(start__range=(start_date, end_date)))
    return HttpResponse(points,content_type='json')


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
