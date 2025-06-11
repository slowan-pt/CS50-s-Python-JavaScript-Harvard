from django.shortcuts import render

from .models import Flight

# Create your views here.
def index (request):
    return render (request, "voos/index.html", {
        "voos": Flight.objects.all(),
        })

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
        return render(request, "voos/flight.html", {
            "voo": flight,  
            "passageiros": flight.passengers.all()  
        })
    except Flight.DoesNotExist:
        return render(request, "voos/not_found.html")