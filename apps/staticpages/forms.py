from django import forms
from django.contrib.auth.models import User
from .models import Profile


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'location', 'bio', 'birth_date', 'picture')
