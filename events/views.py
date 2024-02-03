from django.shortcuts import render, get_object_or_404
from .models import Event, Categories
from django.views.generic.edit import CreateView
from django.http import JsonResponse


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)  # get events by id
    remaining_time = event.time_remaining()
    recent_event = Event.objects.all ( ).order_by ( 'id' )[0 :3]
    context = {
        'events': event,
        'remaining_time': remaining_time,
        'recent_event' : recent_event
    }
    return render(request, 'events/event_detail.html', context)


def event_list(request):
    events = Event.objects.all ( ).order_by ( 'date' )
    category = Categories.objects.all ( ).order_by ( 'id' )[0 :7]
    recent_event = Event.objects.all ( ).order_by ( 'id' )[0 :3]

    context = {
        'events': events,
        'category': category,
        'recent_event' : recent_event

    }
    return render(request, 'events/event_list.html', context)

class EventCreateView(CreateView):
    model = Event
    fields = ['date', 'start_time', 'end_time', 'location', 'title', 'text']

    def form_valid(self, form):
        return super().form_valid(form)

def filter_data(request):

    category_ids = request.GET.getlist('category[]', [])
    filtered_events = Event.objects.filter(category__id__in=category_ids)
    serialized_data = [{'title': event.title, 'date': event.date.strftime('%Y-%m-%d')} for event in filtered_events]

    return JsonResponse({'data': serialized_data})

