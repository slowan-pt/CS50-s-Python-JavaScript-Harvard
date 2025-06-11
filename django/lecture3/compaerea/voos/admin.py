from django.contrib import admin
from .models import Airport, Flight, Passenger

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights',) 

admin.site.register(Airport)
admin.site.register(Flight)