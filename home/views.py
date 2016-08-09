from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import About
from events.models import Event
# Create your views here.
def home(request):
	about_instance = get_object_or_404(About, id=1)
	events = Event.objects.all()
	length_events = len(Event.objects.all())
	base_url = reverse("home")
	home_url="#home"
	about_url="#about"
	events_url="#events"
	donate_url= "#donate"
	context ={
		"about_instance": about_instance,
		"base_url": base_url,
		"events": events,
		"home_url": home_url,
		"about_url": about_url,
		"events_url": events_url,
		"donate_url": donate_url,
		"length_events": length_events,
	}
	return render(request, "base.html", context)




