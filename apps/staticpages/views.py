from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash, authenticate, login
from apps.staticpages.forms import CreateUserForm
from django.contrib import messages
from django.db import transaction
from .forms import *
from django.contrib.auth.decorators import user_passes_test

from social_django.models import UserSocialAuth


def frontpage(request):
    return render(request, "frontpage.html")


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
        PasswordForm = ChangePasswordForm
    else:
        PasswordForm = ChangePasswordForm

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
def update_user(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your user was successfully updated!')
            return redirect('user')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = EditUserForm(instance=request.user)
    return render(request, 'registration/edit_user_form.html', {
        'user_form': user_form,
    })


def register(request):
    if request.user.is_authenticated:
        return redirect('frontpage')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('frontpage')
        else:
            form = CreateUserForm()
        return render(request, 'registration/registration.html', {'form': form})
