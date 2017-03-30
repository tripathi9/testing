from django.contrib import admin

from .models import Event

class EventModelAdmin(admin.ModelAdmin):

    list_display = ("event_name", "event_date" , "address", "date_created", "date_modified")
    list_display_links = ["event_name"]

    list_filter = ["event_date"]
    search_fields = ["event_name", "address"]

    class Meta:
        model=Event
admin.site.register(Event, EventModelAdmin)
