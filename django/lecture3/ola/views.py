from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, "ola/index.html")

def sloan (request):
    return HttpResponse("Ola Http Reponse")

def isabelle (request):
    return HttpResponse("Olá, Isabelle")

def ketelyn (request):
    return HttpResponse("Olá, Ketelyn")

def greet (request, name):
    return render(request, "ola/greet.html", {
        "name": name.capitalize()
    })