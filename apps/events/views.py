from django.shortcuts import render
from .forms import EventForm
from .models import Event, Attendance, Participation
from django.utils import timezone
from django.shortcuts import redirect


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.timestamp = timezone.now()
            event.save()
            return redirect('home')
    form = EventForm(request.POST)
    return render(request, 'events/eventForm.html', {'form':form})