from django.shortcuts import render

from rest_framework import viewsets

from webapp.models import Client, LegalEntity
from webapp.serializers import ClientSerializer, LegalEntitySerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class LegalEntityViewSet(viewsets.ModelViewSet):
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer
