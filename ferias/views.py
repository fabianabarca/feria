from django.shortcuts import render
from django.http import HttpResponse


def openlayers(request):
    context = {'coords_cr': [-84.090725, 9.928069], 'zoom': 13, 'radio': 4000}
    return render(request, 'openlayers.html', context)
