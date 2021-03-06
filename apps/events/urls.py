from django.urls import path
from django.urls import re_path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.user_created, name='user_events'),
    path('new', views.create_event, name='new_event'),
    path('<int:pk>', views.event_detail, name='event_detail'),
    path('<int:pk>/edit/', views.edit_event, name='event_edit'),
    path('test', views.testDjango, name='testDjango'),
    path('pointData', views.showEvents, name='pointData'),
    path('categories', views.showCategories, name='categories'),
    path('timeData/<str:values>/', views.showTime, name='timeData'),
    path('customData/<str:values>/', views.showCustomTime, name='customData'),
    path('listEvents/<str:values>/', views.showRequestedEvents, name='listEvents')
]

