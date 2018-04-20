from django import forms
from .models import *


class EventForm(forms.ModelForm):
    description = forms.CharField(max_length=2000, required=True, widget=forms.Textarea(), help_text='Write the description here!' )

    class Meta:
        model = Event
        exclude =['author', 'timestamp']
        fields = ('title', 'ingress', 'description','start','end','coordinates','address','image','category')

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['ingress'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['start'].widget.attrs.update({'class': 'form-control'})
        self.fields['end'].widget.attrs.update({'class': 'form-control'})
        self.fields['coordinates'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})