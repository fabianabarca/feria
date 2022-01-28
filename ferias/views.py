import os
import json
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ferias.models import Feria
from ferias.utils import is_in_radius, get_provincia_num


def openlayers(request):
    context = {'coords_cr': [-84.090725, 9.928069], 'zoom': 13, 'radio': 4000}
    return render(request, 'openlayers.html', context)

def ferias_detail(request, feria_id, slug = None):
    feria = get_object_or_404(Feria, feria_id=feria_id)
    # convertir a json para poder usarlo con facilidad con JS  
    horarios = json.loads(serializers.serialize("json", feria.horarios.all()))
    context = {
        'feria': feria,
        'horarios': json.dumps(horarios),
        'fotos': feria.fotos.all()
        }
    return render(request, 'ferias_detail.html',context)

def ferias(request):
    query = Q()
    # Input search. We use a OR operator
    query |= Q(nombre__icontains=request.GET.get('search', ''))
    query |= Q(provincia=get_provincia_num(request.GET.get('search', '')))
    query |= Q(canton__icontains=request.GET.get('search', ''))
    query |= Q(distrito__icontains=request.GET.get('search', ''))
    query |= Q(conocida_como__icontains=request.GET.get('search', ''))
    query |= Q(comite__icontains=request.GET.get('search', ''))
    query |= Q(administrador__icontains=request.GET.get('search', ''))

    # Filters. We use a AND operator
    if 'provincia' in request.GET:
        query &= Q(provincia=request.GET.get('provincia', 0))
    if 'canton' in request.GET:
        query &= Q(canton=request.GET.get('canton', ''))
    if 'distrito' in request.GET:
        query &= Q(distrito=request.GET.get('distrito', ''))
    if 'estacionamiento' in request.GET:
        query &= Q(estacionamiento=request.GET.get('estacionamiento', 1))
    if 'parqueo_bicicleta' in request.GET:
        query &= Q(parqueo_bicicleta=request.GET.get('parqueo_bicicleta', 1))
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
        feria_id_filtered = []
        for feria in ferias.iterator():
            # Verificar si esta en el radio
            if is_in_radius(float(lat), float(lon),
                            feria.latitud, feria.longitud,
                            int(radius)):
                # Agregar ID de la feria
                feria_id_filtered.insert(index, feria.feria_id)
                index = index + 1
        # Filtrar las ferias que esten es el radio dado          
        ferias = ferias.filter(feria_id__in=feria_id_filtered)
    # Paginación
    paginator = Paginator(ferias, 10)
    page_number = request.GET.get('page') if 'page' in request.GET else 1
    ferias_paged = paginator.get_page(page_number)

    context = {
        'ferias': ferias_paged
        }
    return render(request, 'ferias_list.html', context)
