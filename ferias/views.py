import math
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from ferias.models import Feria


def openlayers(request):
    context = {'coords_cr': [-84.090725, 9.928069], 'zoom': 13, 'radio': 4000}
    return render(request, 'openlayers.html', context)


def is_in_radius(lat1, lon1, lat2, lon2, radius):
    """ Calcular distancia de dos coordenadas usando la formula Haversine
            https://www.movable-type.co.uk/scripts/latlong.html
        """

    radius_earth = 6371e3  # Radio de la tierra en metros
    pi_radian = (math.pi/180)
    phi_1 = lat1 * pi_radian
    phi_2 = lat2 * pi_radian
    delta_phi = (lat2 - lat1) * pi_radian
    delta_lambda = (lon2 - lon1) * pi_radian

    a = math.sin(delta_phi/2)**2 + math.cos(phi_1) * \
        math.cos(phi_2) * math.sin(delta_lambda/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius_earth * c
    if distance <= radius:
        return True
    else:
        return False


def ferias(request):
    query = Q()
    # Input search
    query &= Q(nombre__contains=request.GET.get('search', ''))
    # query != Q(conocida_como__contains=request.GET.get('search', ''))
    # query != Q(comite__contains=request.GET.get('search', ''))

    # Filters
    if 'provincia' in request.GET:
        query &= Q(provincia=request.GET.get('provincia', 0))
    if 'canton' in request.GET:
        query &= Q(canton=request.GET.get('canton', ''))
    if 'distrito' in request.GET:
        query &= Q(distrito=request.GET.get('distrito', ''))
    if 'parqueo' in request.GET:
        query &= Q(parqueo=request.GET.get('parqueo', 1))
    if 'parqueo_bici' in request.GET:
        query &= Q(parqueo_bici=request.GET.get('parqueo_bici', 1))
    if 'sanitarios' in request.GET:
        query &= Q(sanitarios=request.GET.get('sanitarios', 1))
    if 'bajo_techo' in request.GET:
        query &= Q(bajo_techo=request.GET.get('bajo_techo', 1))
    if 'campo_ferial' in request.GET:
        query &= Q(campo_ferial=request.GET.get('campo_ferial', 1))
    if 'agua_potable' in request.GET:
        query &= Q(agua_potable=request.GET.get('agua_potable', 1))
    if 'accesibilidad' in request.GET:
        query &= Q(accesibilidad=request.GET.get('accesibilidad', 1))

    ferias = Feria.objects.filter(query)
    # Filtrar por latitud, longitud y radio
    if 'lat' in request.GET and 'lon' in request.GET and 'radius' in request.GET:
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        radius = request.GET.get('radius')
        index = 0
        ferias_id_filtered = []
        for feria in ferias.iterator():
            # Verificar si esta en el radio
            if is_in_radius(float(lat), float(lon),
                            feria.latitud, feria.longitud,
                            int(radius)):
                # Agregar ID de la feria
                ferias_id_filtered.insert(index, feria.ferias_id)
                index = index + 1
            # Filtrar las ferias que esten es el radio dado
            print(ferias_id_filtered)
        ferias = ferias.filter(ferias_id__in=ferias_id_filtered)
    context = {'ferias': ferias}
    return render(request, 'ferias.html', context)
