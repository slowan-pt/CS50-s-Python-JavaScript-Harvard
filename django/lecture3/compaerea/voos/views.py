from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

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
            "passageiros": flight.passengers.all(),
            "sem_passageiros": Passenger.objects.exclude(flights=flight).all()  # Mantido como sem_passageiros
        })
    except Flight.DoesNotExist:
        return render(request, "voos/not_found.html")
    
def book(request, flight_id):
    if request.method == "POST":
        try:
            flight = Flight.objects.get(pk=flight_id)
            passenger = Passenger.objects.get(pk=int(request.POST["passenger_id"]))  
            passenger.flights.add(flight)
            return HttpResponseRedirect(reverse("flight", args=(flight_id,)))  
        except (Flight.DoesNotExist, Passenger.DoesNotExist, KeyError, ValueError) as e:
            return render(request, "voos/error.html", {
                "message": "Erro ao reservar voo. Verifique os dados e tente novamente."
            })