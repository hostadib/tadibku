from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import EventCreateView, filter_data

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('events/<slug:slug>', views.event_detail, name='event_detail'),  # This is for events
    path('events/new/', EventCreateView.as_view(), name='event_new'),
    path('filter_data/', filter_data, name='filter_data'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
