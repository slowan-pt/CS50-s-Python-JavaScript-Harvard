from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index (request):
    return HttpResponse("Olá, mundo!")

def sloan (request):
    return HttpResponse("Ola Http Reponse")

def isabelle (request):
    return HttpResponse("Olá, Isabelle")

def ketelyn (request):
    return HttpResponse("Olá, Ketelyn")

def greet (request, name):
    return HttpResponse(f"Olá, {name.capitalize()}!")