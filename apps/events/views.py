from django.shortcuts import render, get_object_or_404
from .forms import EventForm
from .models import Event, Attendance, Participation
from django.utils import timezone
from django.shortcuts import redirect


def interface(request):
    return render(request, 'events/eventInterface.html')


def create_event(request):
    action = 'Create new'
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.timestamp = timezone.now()
            event.save()
            attendance = Attendance.objects.create(event=event)
            participation = Participation.objects.create(attendance=attendance, user=request.user, status='G')
            attendance.save()
            participation.save()
            return redirect('events:interface')
    form = EventForm(request.POST)
    return render(request, 'events/eventForm.html', {
        'form':form,
        'action':action
    })


def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    owner = event.author
    action = 'Edit'
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.timestamp = timezone.now()
            event.save()
            return redirect('events:event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
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
