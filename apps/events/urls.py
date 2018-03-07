from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('', views.interface, name='interface'),
    path('new', views.create_event, name='new_event'),
    path('list', views.user_created, name='user_events'),
    path('<int:pk>', views.event_detail, name='event_detail')
]