from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	event_date = models.DateTimeField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	facebook_event = models.URLField(blank=True)
	external_link_text= models.CharField(blank=True, max_length=50)
	external_link = models.URLField(blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("event_view", kwargs={'id': self.id})


	class Meta:
	 	ordering = ["-event_date", "-timestamp"]