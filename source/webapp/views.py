from django.shortcuts import render

from rest_framework import viewsets

from webapp.models import Client
from webapp.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    serializer_class = ClientSerializer

