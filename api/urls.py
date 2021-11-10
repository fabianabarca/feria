from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import feria_views, producto_views, horario_view

urlpatterns = [
    path('productos/', producto_views.ProductoList().as_view()),
    path('productos/<int:pk>/', producto_views.ProductoDetail().as_view()),
    path('ferias/', feria_views.FeriaList().as_view()),
    path('ferias/<slug:pk>/', feria_views.FeriaDetail().as_view()),
    path('horarios/<slug:pk>/', horario_view.HorarioDetail().as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
