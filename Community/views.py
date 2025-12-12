from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from .forms import EventForm
from .models import Event
# Create your views here.

def all_Events(request):
    events = Event.objects.all()
    return render(request, "Community/index.html",{
        'events': events
    })

def event_Details(request,pk):
    event = get_object_or_404(Event, pk=pk)

    return render(request, "Community/eventDetail.html",{
        "event": event
     })



class EventFormView(FormView):
    template_name = "Community/Eventform.html"
    form_class = EventForm
    success_url = "/"

    def form_valid(self, form):
        event = form.save(commit=False)
        event.save()
        return super().form_valid(form)
    