from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Event

# Create your views here.
def event_view(request, id):
	instance = get_object_or_404(Event, id=id)
	home_url= str(reverse("home"))+"#home"
	about_url= str(reverse("home"))+"#about"
	events_url= str(reverse("home"))+"#events"
	donate_url = str(reverse("home"))+"#donate"
	print(home_url)
	context={
		"instance": instance,
		"home_url": home_url,
		"about_url": about_url,
		"events_url": events_url,
		"donate_url": donate_url,
	}
	return render(request, "event_view.html", context)