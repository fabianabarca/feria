from django.urls import path
import drf_spectacular.views as spect
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import feria_views, producto_views, horario_view

urlpatterns = [
    # API Endpoints
    path('productos/', producto_views.ProductoList().as_view()),
    path('productos/<int:pk>/', producto_views.ProductoDetail().as_view()),
    path('ferias/', feria_views.FeriaList().as_view()),
    path('ferias/<slug:pk>/', feria_views.FeriaDetail().as_view()),
    path('horarios/<slug:pk>/', horario_view.HorarioDetail().as_view()),
    # OpenAPI Endpoints:
    path(
        'doc/', spect.SpectacularAPIView.as_view(), name='schema'),
    path('doc/swagger-ui/',
         spect.SpectacularSwaggerView.as_view(
             url_name='schema'), name='swagger-ui'),
    path('doc/redoc/',
         spect.SpectacularRedocView.as_view(
             template_name='redoc.html'), name='redoc'),
    path('doc/swagger.json',
         spect.SpectacularJSONAPIView.as_view(), name='swagger-json'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
