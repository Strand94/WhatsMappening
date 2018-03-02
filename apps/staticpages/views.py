from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.db import transaction
from .forms import *

from social_django.models import UserSocialAuth



def frontpage(request):
    return render(request, "frontpage.html")

@login_required
def home(request):
    return render(request, 'staticpages/home.html')

@login_required
def user(request):
    return render(request, 'staticpages/userpage.html')

@login_required
def settings(request):
    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'registration/settings.html', {
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'registration/password.html', {'form': form})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('user')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
    return render(request, 'registration/edit_user_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
