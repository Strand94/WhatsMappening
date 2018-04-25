from django import forms
from .models import *
from django.contrib.admin import widgets
from leaflet.forms.fields import PointField


class EventForm(forms.ModelForm):
    description = forms.CharField(max_length=2000, required=True, widget=forms.Textarea(), help_text='Write the description here!' )
    startDate = forms.DateField(required=True, widget=widgets.AdminDateWidget())
    startTime = forms.TimeField(required=True, widget=widgets.AdminTimeWidget())
    endDate = forms.DateField(required=True, widget=widgets.AdminDateWidget())
    endTime = forms.TimeField(required=True, widget=widgets.AdminTimeWidget())
    location = PointField()

    class Meta:
        model = Event
        exclude =['author', 'timestamp', 'start', 'end']
        fields = ('title', 'ingress', 'description','startTime','startDate','endTime','endDate','coordinates','address','image','category', 'location')

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['ingress'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['coordinates'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
