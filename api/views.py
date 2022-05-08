from ferias.models import Producto, Feria
from api.serializers import ProductoSerializer, FeriaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#
#====================FERIA===========================
#
class FeriaList(APIView):
    def get(self, request, format=None):
        productos = Feria.objects.all()
        serializer = FeriaSerializer(productos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeriaDetail(APIView):
    def get_object(self, pk):
        try:
            return Feria.objects.get(feria_id=pk)
        except Feria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        feria = self.get_object(pk)
        print(feria)
        serializer = FeriaSerializer(feria)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        feria = self.get_object(pk)
        serializer = FeriaSerializer(feria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        feria = self.get_object(pk)
        feria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
#====================PRODUCTO===========================
#
class ProductoList(APIView):
    def get(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoDetail(APIView):
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        producto = self.get_object(pk)
        print(producto)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


