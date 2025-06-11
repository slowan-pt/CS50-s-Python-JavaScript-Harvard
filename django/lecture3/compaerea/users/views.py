from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return HttpResponseRedirect(reverse("user"))
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Usuário ou senha inválidos."
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Você foi desconectado."
    })

def user_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")