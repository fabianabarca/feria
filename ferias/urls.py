from django.urls import path

from . import views

urlpatterns = [
    path('', views.openlayers, name='openlayers'),
]
