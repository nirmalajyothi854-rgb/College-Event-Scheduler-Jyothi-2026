from django.contrib import admin

from .models import Event, Activity, Registration


admin.site.register(Event)

admin.site.register(Activity)

admin.site.register(Registration)