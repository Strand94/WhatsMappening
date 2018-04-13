from django.urls import path
from . import views
from djgeojson.views import GeoJSONLayerView
from . models import SimpleEvent2

app_name = 'job'

urlpatterns = [
    path('', views.user_created, name='user_events'),
    path('new', views.create_event, name='new_event'),
    path('<int:pk>', views.event_detail, name='event_detail'),
    path('<int:pk>/edit/', views.edit_event, name='event_edit'),
    path('test', views.testDjango, name='testDjango'),
    path('pointData', views.showEvents, name='pointData'),
    path('categories', views.showCategories, name='categories'),
    path('data', GeoJSONLayerView.as_view(model=SimpleEvent2, properties=('title')), name='data')
]