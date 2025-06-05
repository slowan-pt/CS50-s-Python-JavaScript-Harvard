from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index, name="index"),
    path ("<str:name>", views.greet, name="greet"),
    path ("sloan", views.sloan, name="sloan"),
    path ("isabelle", views.isabelle, name="isabelle"),
    path ("ketelyn", views.ketelyn, name="ketelyn")
]