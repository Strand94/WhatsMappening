from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.interface, name='interface'),
    path('new', views.create_event, name='new_event'),
    path('test', views.testDjango, name='testDjango'),
    path('pointData', views.showEvents, name='pointData'),
    path('categories', views.showCategories, name='categories'),
]