import datetime
from django.shortcuts import render

# Create your views here.
def index (request):
    hoje = datetime.datetime.now()
    return render(request, "anonovo/index.html", {
        "anonovo": hoje.month == 1 and hoje.day == 1
    })