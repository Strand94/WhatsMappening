from django import forms
from .models import *
from datetimewidget.widgets import DateTimeWidget
from leaflet.forms.fields import PointField


class EventForm(forms.ModelForm):
    description = forms.CharField(max_length=2000, required=True, widget=forms.Textarea(), help_text='Write the description here!' )
    location = PointField(help_text="click the marker icon and place it in the desired location")

    class Meta:
        model = Event
        widgets = {
            # Use localization and bootstrap 3
            'start': DateTimeWidget(attrs={'id': "start"}, usel10n=True, bootstrap_version=3),
            'end': DateTimeWidget(attrs={'id': "start"}, usel10n=True, bootstrap_version=3),

        }
        exclude =['author', 'timestamp']
        fields = ('title', 'ingress', 'description','start','end','address','image','category', 'location')

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['ingress'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
