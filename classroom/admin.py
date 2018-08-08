from django.contrib import admin

from .models import School, Location, Instance, Event


admin.site.register(School)
admin.site.register(Location)
admin.site.register(Instance)
admin.site.register(Event)
