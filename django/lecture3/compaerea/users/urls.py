from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('user/', views.user_view, name='user'),  # Nova rota
    path('logout/', views.logout_view, name='logout')
]