from django.contrib import admin

# Register your models here.
from .models import About

class AboutAdmin(admin.ModelAdmin):
	list_display = ["title1", "title2", "timestamp", "updated"]
	# readonly_fields=('title1', "title2")
	class Meta:
		model = About

admin.site.register(About, AboutAdmin)
