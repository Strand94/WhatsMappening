from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def frontpage(request):
    return render(request, "frontpage.html")

@login_required
def home(request):
    return render(request, 'staticpages/home.html')