from django.shortcuts import render

tarefas = ["Tarefa1", "a fazer", "Tarefa3"]
# Create your views here.
def index (request):
    return render(request, "tarefas/index.html", {
        "tarefas": tarefas
    })

def adicionar (request):
    return render (request, "tarefas/adicionar.html")
