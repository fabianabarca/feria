from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import feria_views, producto_views, horario_view

urlpatterns = [
    path('productos/', producto_views.ProductoList().as_view()),
    path('productos/<int:pk>/', producto_views.ProductoDetail().as_view()),
    path('ferias/', feria_views.FeriaList().as_view()),
    path('ferias/<slug:pk>/', feria_views.FeriaDetail().as_view()),
    path('horarios/<slug:pk>/', horario_view.HorarioDetail().as_view()),    
    path(
        'doc/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    # path('doc/swagger-ui/',
    #      SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('doc/redoc/',
         SpectacularRedocView.as_view(), name='redoc'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
