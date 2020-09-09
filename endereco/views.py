from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import  GenericViewSet
from endereco.models import Estado
from endereco.serializers import EstadoSerializer


class EstadoViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
