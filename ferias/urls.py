from django.urls import path

from . import views

urlpatterns = [
    path('', views.ferias, name='list-ferias'),
]
