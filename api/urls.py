from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('productos/', views.ProductoList().as_view()),
    path('productos/<int:pk>/', views.ProductoDetail().as_view()),
    path('ferias/', views.FeriaList().as_view()),
    path('ferias/<slug:pk>/', views.FeriaDetail().as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
