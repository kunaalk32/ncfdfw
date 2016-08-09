from __future__ import unicode_literals

from django.db import models

# Create your models here.
class About(models.Model):
	title1 = models.CharField(max_length=25, default="What is Ewing's Sarcoma")
	content1 = models.TextField()
	title2 = models.CharField(max_length=22, default="About the Foundation")
	content2 = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "About"