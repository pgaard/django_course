from django.contrib import admin
from .models import Meetup, Location, Participant
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location') # columns in the admin
    list_filter = ('location', 'date') # filterable columns
    prepopulated_fields = { 'slug': ('title',) }  # make the slug auto populate based on the title

# define which fields will show up in admin
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)