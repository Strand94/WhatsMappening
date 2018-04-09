from django.urls import path
from . import views
from djgeojson.views import GeoJSONLayerView
from . models import SimpleEvent2

app_name = 'job'

urlpatterns = [
    path('', views.interface, name='interface'),
    path('new', views.create_event, name='new_event'),
    path('test', views.testDjango, name='testDjango'),
    path('pointData', views.showEvents, name='pointData'),
    path('categories', views.showCategories, name='categories'),
    path('data', GeoJSONLayerView.as_view(model=SimpleEvent2, properties=('title')), name='data')
]